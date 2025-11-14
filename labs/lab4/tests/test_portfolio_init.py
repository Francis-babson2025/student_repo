
from portfolio import Portfolio

def test_portfolio_init():
    print("Running test_portfolio_init()...")
    try:
        p = Portfolio("Bob")
    except NotImplementedError:
        assert False, "__init__ not implemented yet"
    assert p.name == "Bob"
    assert isinstance(p.positions, list)
    assert p.cash == 0.0
    print("✅ test_portfolio_init passed")
