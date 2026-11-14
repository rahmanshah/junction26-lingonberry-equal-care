"""The app's one-line core message, and the ledger claims behind each part of it.

Each part names its supporting claims either by ID or by (source document, opening words of a quote),
so the backing survives ledger rebuilds (quote IDs are hashes). src/check_claims.py fails if any part
does not resolve to existing, citable claims.
"""
import ledger
import sources

MESSAGE = ("Finland's cancer strategy sets a target for timely access to treatment, "
           "but the national lung cancer report publishes no access times for any county.")

STRATEGY = "data/raw/strategy_2026_2035_fi.pdf"
PARTS = [
    ("Finland's cancer strategy sets a target for timely access to treatment",
     # Strategy p.5: indicator "patients access care within the target times", footnoted to THL 21/2016.
     [("quote", STRATEGY, "Potilaat pääsevät hoitoon tavoiteaikojen puitteissa***"),
      ("quote", STRATEGY, "*** THL (Ohjaus 21/2016)")]),
    ("the national lung cancer report publishes no access times for any county",
     # Blind-spot table (from the 2019–2023 report): referral not measured; first visit and treatment
     # start: whether, never when.
     [("id", "bs:coverage:Referral"), ("id", "bs:coverage:First_specialist_visit"),
      ("id", "bs:coverage:Treatment_start")]),
]


def resolve(claims: dict[str, dict]) -> tuple[list[tuple[str, list[str]]], list[str]]:
    """[(part text, [claim ids])] and a list of problems (unresolved or not citable)."""
    out, problems = [], []
    for text, refs in PARTS:
        ids = []
        for ref in refs:
            if ref[0] == "id":
                hits = [ref[1]] if ref[1] in claims else []
            else:
                _, src, prefix = ref
                key = sources.normalise(prefix)
                hits = [cid for cid, c in claims.items() if c.get("quote") and c["source_doc"] == src
                        and sources.normalise(c["quote"]).startswith(key)]
            if not hits:
                problems.append(f"core message part {text!r}: no claim for {ref[1:]}")
            for cid in hits:
                if claims[cid]["status"] not in ledger.CITABLE:
                    problems.append(f"core message part {text!r}: claim {cid} is {claims[cid]['status']!r}")
                elif cid not in ids:
                    ids.append(cid)
        out.append((text, ids))
    return out, problems
