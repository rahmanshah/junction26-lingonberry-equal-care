"""County names: short (nominative) name -> name as printed in the report's Taulukko 11."""
import re

FULL = {
    "Etelä-Karjala": "Etelä-Karjalan hyvinvointialue",
    "Helsinki": "Helsingin kaupunki",
    "Itä-Uusimaa": "Itä-Uudenmaan hyvinvointialue",
    "Keski-Uusimaa": "Keski-Uudenmaan hyvinvointialue",
    "Kymenlaakso": "Kymenlaakson hyvinvointialue",
    "Länsi-Uusimaa": "Länsi-Uudenmaan hyvinvointialue",
    "Päijät-Häme": "Päijät-Hämeen hyvinvointialue",
    "Vantaa ja Kerava": "Vantaan ja Keravan hyvinvointialue",
    "Etelä-Savo": "Etelä-Savon hyvinvointialue",
    "Keski-Suomi": "Keski-Suomen hyvinvointialue",
    "Pohjois-Karjala": "Pohjois-Karjalan hyvinvointialue",
    "Pohjois-Savo": "Pohjois-Savon hyvinvointialue",
    "Pohjanmaa": "Pohjanmaan hyvinvointialue",
    "Satakunta": "Satakunnan hyvinvointialue",
    "Varsinais-Suomi": "Varsinais-Suomen hyvinvointialue",
    "Kainuu": "Kainuun hyvinvointialue",
    "Keski-Pohjanmaa": "Keski-Pohjanmaan hyvinvointialue",
    "Lappi": "Lapin hyvinvointialue",
    "Pohjois-Pohjanmaa": "Pohjois-Pohjanmaan hyvinvointialue",
    "Etelä-Pohjanmaa": "Etelä-Pohjanmaan hyvinvointialue",
    "Kanta-Häme": "Kanta-Hämeen hyvinvointialue",
    "Pirkanmaa": "Pirkanmaan hyvinvointialue",
}
SHORT = {v: k for k, v in FULL.items()}


def resolve(name: str) -> tuple[str, str]:
    """(short name, full name) for a short or full county name, case-insensitive."""
    for short, full in FULL.items():
        if name.casefold() in (short.casefold(), full.casefold()):
            return short, full
    raise SystemExit(f"Unknown county {name!r}. Use one of: {', '.join(FULL)}")


def slug(short: str) -> str:
    table = str.maketrans({"ä": "a", "ö": "o", "å": "a", "Ä": "a", "Ö": "o"})
    return re.sub(r"[^a-z0-9]+", "-", short.translate(table).lower()).strip("-")
