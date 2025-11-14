
from portfolio import Portfolio

def test_portfolio_str():
    print("Running test_portfolio_str()...")
    p = Portfolio("Bob")
    p.positions = []
    p.cash = 1234.56
    try:
        s = str(p)
    except NotImplementedError:
        assert False, "__str__ not implemented yet"
    assert "Bob" in s
    assert ("1234.56" in s) or ("1,234.56" in s)
    print("✅ test_portfolio_str passed")
