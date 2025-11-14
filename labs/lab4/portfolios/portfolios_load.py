# Get the lab4 directory (one above 'portfolios')

from portfolio import Portfolio
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

def portfolios_load(self, filename: str = "clients.json"):
    path = DATA_DIR / filename   # always correct regardless of terminal location

    if not path.exists():
        self.clients = {}
        return self

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    self.clients = {}
    for name, pd in data.items():
        p = Portfolio(name)
        p.cash = float(pd.get("cash", 0.0))
        p.positions = list(pd.get("positions", []))
        self.clients[name] = p

    return self