
import prices
from portfolio import Portfolio

def test_sell_stock():
    prices.get_last_close_map = lambda syms: {syms[0]: 50.0}
    p = Portfolio("Bob")
    p.cash = 0.0
    p.positions = [{"sym":"AAPL","name":"Apple","shares":10,"cost":500.0}]
    try:
        p.sell_stock("AAPL", 5, 50.00)
    except NotImplementedError:
        assert False, "sell_stock not implemented yet"
    assert p.cash == 250.0
    assert p.positions[0]["shares"] == 5
    assert abs(p.positions[0]["cost"] - 250.0) < 1e-9
