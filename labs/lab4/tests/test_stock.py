
from portfolio.stock import Stock

def test_stock_todo_init_and_str():
    print("Running test_stock_todo_init_and_str()...")
    try:
        s = Stock("AAPL", "Apple Inc.", 10, 1500.0)
        out = str(s)
    except NotImplementedError:
        assert False, "Stock TODOs not implemented yet"
    assert "AAPL" in out, "symbol missing"
    assert "10" in out, "shares missing"
    assert ("1500" in out) or ("1,500" in out), "cost missing"
    print("✅ test_stock_todo_init_and_str passed")
