"""Thin wrapper around google-genai: one structured call, raw response saved to disk.

Every call's full request (prompt, model, config) and raw response are written to
data/processed/gemini_raw/<tag>_<UTC time>.json. The API key is read from .env and never written.
"""
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

RAW_DIR = Path("data/processed/gemini_raw")
load_dotenv()


def model_name(env_var: str) -> str:
    name = os.environ.get(env_var)
    if not name:
        raise SystemExit(f"{env_var} missing from .env")
    return name


def client() -> genai.Client:
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise SystemExit("GEMINI_API_KEY missing from .env")
    return genai.Client(api_key=key)


def structured_call(model: str, system: str, prompt: str, schema: type[BaseModel], tag: str,
                    thinking_level: str | None = None) -> tuple[BaseModel | None, str, Path]:
    """Call `model` with JSON output matching `schema`. Returns (parsed, raw text, raw file path)."""
    config = types.GenerateContentConfig(
        system_instruction=system,
        response_mime_type="application/json",
        response_schema=schema,
        temperature=0.2,
        thinking_config=types.ThinkingConfig(thinking_level=thinking_level) if thinking_level else None,
    )
    started = datetime.now(timezone.utc)
    response = client().models.generate_content(model=model, contents=prompt, config=config)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = RAW_DIR / f"{tag}_{started.strftime('%Y%m%dT%H%M%SZ')}.json"
    record = {
        "tag": tag, "model": model, "requested_at": started.isoformat(),
        "config": {"thinking_level": thinking_level, "temperature": 0.2,
                   "response_schema": schema.__name__},
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
