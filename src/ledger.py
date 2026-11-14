"""Claim ledger: data/ledger.sqlite with one table, `claims`.

Every number or statement used in the brief gets a row: what is claimed, where it comes from
(source_doc + location), how we got it (method) and how sure we are (status).

  method: computed   our own code from published counts (e.g. shares, Wilson CIs)
          digitised  read off a published figure by our code (src/digitise_kuva16.py)
          quoted     verbatim text from a source; `quote` must be found in source_doc at location
          mentor     expert input without a written source
          assessed   our judgement from reading a source (e.g. "stage X is not measured")
  status: verified locally | verified by Hellu | preliminary | mentor insight | draft

Run directly to (re)create an empty ledger. src/load_claims.py fills it.
"""
import sqlite3
from pathlib import Path

DB = Path("data/ledger.sqlite")
METHODS = ("computed", "digitised", "quoted", "mentor", "assessed")
STATUSES = ("verified locally", "verified by Hellu", "preliminary", "mentor insight", "draft")

SCHEMA = f"""
CREATE TABLE claims (
    id          TEXT PRIMARY KEY,
    claim_text  TEXT NOT NULL,
    value       REAL,
    unit        TEXT,
    county      TEXT,
    metric      TEXT,
    source_doc  TEXT,
    location    TEXT,
    quote       TEXT,
    method      TEXT NOT NULL CHECK (method IN ({", ".join(repr(m) for m in METHODS)})),
    status      TEXT NOT NULL CHECK (status IN ({", ".join(repr(s) for s in STATUSES)})),
    notes       TEXT
);
"""
COLUMNS = ("id", "claim_text", "value", "unit", "county", "metric", "source_doc", "location",
           "quote", "method", "status", "notes")


def create(path: Path = DB) -> sqlite3.Connection:
    """Create a fresh, empty ledger (replaces any existing file)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        path.unlink()
    con = sqlite3.connect(path)
    con.executescript(SCHEMA)
    return con


def insert(con: sqlite3.Connection, rows: list[dict]) -> None:
    ids = [r["id"] for r in rows]
    dupes = {i for i in ids if ids.count(i) > 1}
    assert not dupes, f"Duplicate claim ids: {sorted(dupes)[:5]}"
    con.executemany(
        f"INSERT INTO claims ({', '.join(COLUMNS)}) VALUES ({', '.join('?' * len(COLUMNS))})",
        [tuple(r.get(c) for c in COLUMNS) for r in rows],
    )
    con.commit()


if __name__ == "__main__":
    create().close()
    print("Created empty", DB)
