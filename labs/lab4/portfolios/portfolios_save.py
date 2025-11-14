import json
from pathlib import Path

# ROOT is the student-repo directory (3 levels up)
ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "data"    # student-repo/data

def portfolios_save(self, filename: str = "clients.json"):
    """
    Save portfolios to JSON file in student-repo/data/clients.json.
    """

    # Build client structure
    clients = {}
    for name, portfolio in self.clients.items():
        clients[name] = {
            "cash": portfolio.cash,
            "positions": portfolio.positions
        }

    # Full path to data file
    path = DATA_DIR / filename

    # Save JSON
    with open(path, "w", encoding="utf-8") as f:
        json.dump(clients, f, indent=2)

    return True
