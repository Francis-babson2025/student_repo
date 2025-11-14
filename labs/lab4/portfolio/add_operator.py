
def portfolio_add_operator(self, other): 
    """TODO: Return a NEW Portfolio with merged positions and cash.
    - client name: f"{self.client}+{other.client}"
    - cash = self.cash + other.cash
    - positions merged per symbol (shares and cost added)
    """
    

    # ✅ Proper Python behavior for unsupported types
    from portfolio import Portfolio
    if not isinstance(other, Portfolio):
        return NotImplemented

    # Create new combined portfolio
    new_name = f"{self.name}+{other.name}"
    new_port = Portfolio(new_name)

    # ---- Combine cash ------------------------------------------------------
    new_port.cash = float(self.cash) + float(other.cash)

    # ---- Merge positions ---------------------------------------------------
    merged = {}

    # Add positions from self
    for pos in self.positions:
        sym = pos["sym"]
        merged[sym] = {
            "sym": sym,
            "name": pos["name"],
            "shares": pos["shares"],
            "cost": pos["cost"]
        }

    # Add or merge positions from other
    for pos in other.positions:
        sym = pos["sym"]
        if sym not in merged:
            merged[sym] = {
                "sym": sym,
                "name": pos["name"],
                "shares": pos["shares"],
                "cost": pos["cost"]
            }
        else:
            merged[sym]["shares"] += pos["shares"]
            merged[sym]["cost"] += pos["cost"]

    # Save as list
    new_port.positions = list(merged.values())

    return new_port
