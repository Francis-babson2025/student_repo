
from portfolio import Portfolio

def test_add_cash():
    p = Portfolio("Bob"); p.cash = 100.0; p.positions = []
    try:
        p.add_cash(50.0)
    except NotImplementedError:
        assert False, "add_cash not implemented yet"
    assert p.cash == 150.0
