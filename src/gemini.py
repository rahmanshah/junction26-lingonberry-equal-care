"""Thin wrapper around google-genai: one structured call, raw response saved to disk.

Every call's full request (prompt, model, config) and raw response are written to
data/processed/gemini_raw/<tag>_<UTC time>.json. The API key is read from .env and never written.
"""
import json
import os
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import errors as genai_errors
from google.genai import types
from pydantic import BaseModel

RAW_DIR = Path("data/processed/gemini_raw")
load_dotenv()


def model_name(env_var: str) -> str:
    name = os.environ.get(env_var)
    if not name:
        raise SystemExit(f"{env_var} missing from .env")
    return name


_CLIENT: genai.Client | None = None
_CLIENT_LOCK = threading.Lock()


def client() -> genai.Client:
    """One client per process (a temporary client is closed when garbage-collected). Created under a
    lock: without it, parallel threads each create one and the discarded ones close mid-request."""
    global _CLIENT
    with _CLIENT_LOCK:
        if _CLIENT is None:
            key = os.environ.get("GEMINI_API_KEY")
            if not key:
                raise SystemExit("GEMINI_API_KEY missing from .env")
            _CLIENT = genai.Client(api_key=key)
        return _CLIENT


TRANSIENT = {429, 500, 502, 503, 504}


def is_transient(e: Exception) -> bool:
    """Rate limit / overload (API status code) or a dropped connection raised by the SDK's HTTP layer
    (e.g. RemoteProtocolError: server disconnected). The HTTP package is an SDK internal, so it is
    recognised by module name rather than imported."""
    if isinstance(e, genai_errors.APIError):
        return getattr(e, "code", None) in TRANSIENT
    return type(e).__module__.split(".")[0].startswith(("httpx", "httpcore"))


def structured_call(model: str, system: str, prompt: str, schema: type[BaseModel], tag: str,
                    thinking_level: str | None = None, temperature: float = 0.2,
                    seed: int | None = None, retries: int = 4) -> tuple[BaseModel | None, str, Path]:
    """Call `model` with JSON output matching `schema`. Returns (parsed, raw text, raw file path).
    Transient API errors (rate limit, overload) are retried with exponential backoff."""
    settings = {"temperature": temperature, "seed": seed, "thinking_level": thinking_level,
                "response_schema": schema.__name__}
    config = types.GenerateContentConfig(
        system_instruction=system,
        response_mime_type="application/json",
        response_schema=schema,
        temperature=temperature,
        seed=seed,
        thinking_config=types.ThinkingConfig(thinking_level=thinking_level) if thinking_level else None,
    )
    started = datetime.now(timezone.utc)
    for attempt in range(retries + 1):
        try:
            response = client().models.generate_content(model=model, contents=prompt, config=config)
            break
        except Exception as e:  # noqa: BLE001 - re-raised below unless transient
            if not is_transient(e) or attempt == retries:
                raise
            time.sleep(15 * 2 ** attempt)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = RAW_DIR / f"{tag}_{started.strftime('%Y%m%dT%H%M%S%fZ')}.json"
    record = {
        "tag": tag, "model": model, "requested_at": started.isoformat(),
        "model_version": getattr(response, "model_version", None), "config": settings,
        "system_instruction": system, "prompt": prompt,
        "response": response.model_dump(mode="json", exclude_none=True),
    }
    path.write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
    parsed = response.parsed if isinstance(response.parsed, schema) else None
    if parsed is None and response.text:
        try:
            parsed = schema.model_validate_json(response.text)
        except ValueError:
            parsed = None
    return parsed, response.text or "", path
