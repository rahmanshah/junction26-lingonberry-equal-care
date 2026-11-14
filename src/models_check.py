"""Smoke test: is the Gemini key valid, which models can we use, does a call work?"""
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("GEMINI_API_KEY missing. Check that .env is in the repo root.")

client = genai.Client(api_key=api_key)

# 1. Which models does this key see?
names = [m.name for m in client.models.list()]
interesting = [n for n in names if "gemini-4" in n or "gemini-3.8" in n]
print("Models available to this key:")
for n in interesting:
    print("  ", n)
print("Carbon available:", any("carbon" in n for n in names))

# 2. One tiny call to the model we plan to use
model = os.environ.get("MODEL_EXTRACT", "gemini-4-argon")
response = client.models.generate_content(
    model=model,
    contents="Reply with the single word: ok",
)
print(f"{model} says:", response.text)