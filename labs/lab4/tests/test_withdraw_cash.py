
from portfolio import Portfolio

def test_withdraw_cash():
    p = Portfolio("Bob"); p.cash = 100.0; p.positions = []
    try:
        p.withdraw_cash(30.0)
    except NotImplementedError:
        assert False, "withdraw_cash not implemented yet"
    assert p.cash == 70.0
