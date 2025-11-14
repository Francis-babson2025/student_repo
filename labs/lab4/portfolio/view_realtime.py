import prices as _prices

def portfolio_view_realtime(self):
    """
    Returns: dict mapping symbol -> realtime price (for tests).
    Printing is handled in main via a shared renderer.
    """
    syms = [pos["sym"] for pos in self.positions]
    px_map = _prices.get_live_map(syms)
    return px_map
