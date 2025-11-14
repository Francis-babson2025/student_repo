
import prices
from portfolio import Portfolio

def test_view_last_close_runs_and_returns_map():
    prices.get_last_close_map = lambda syms: {sym: 10.0 for sym in syms}
    p = Portfolio("Bob")
    p.positions = [{"sym":"AAPL","name":"Apple","shares":5,"cost":500.0}]
    try:
        px = p.view_portfolio_last_close()
    except NotImplementedError:
        assert False, "view_portfolio_last_close not implemented yet"
    assert isinstance(px, dict) and "AAPL" in px
