
import prices
from portfolio import Portfolio

def test_view_realtime_runs_and_returns_map():
    prices.get_live_map = lambda syms: {sym: 12.0 for sym in syms}
    p = Portfolio("Bob")
    p.positions = [{"sym":"AAPL","name":"Apple","shares":5,"cost":500.0}]
    try:
        px = p.view_portfolio_realtime()
    except NotImplementedError:
        assert False, "view_portfolio_realtime not implemented yet"
    assert isinstance(px, dict) and "AAPL" in px and px["AAPL"] == 12.0
