from portfolio import Portfolio
import prices 

def test_buy_stock():
    """
    The buy_stock test allows flexibility in price.
    Price must be within 10% of the expected mock value.
    """
    p = Portfolio("Alice")
    p.cash = 10000

    # expected mock price range
    expected = float(prices.SAMPLE_PRICES["AAPL"])
    lower = expected * 0.90
    upper = expected * 1.10

    # inject a predictable closing price
    def fake_close_map(symbols):
        return {symbols[0]: 100}

    prices.get_last_close_map = fake_close_map

    p.buy_stock("AAPL", 10, expected)

    # validate structure
    assert len(p.positions) == 1
    pos = p.positions[0]
    price_used = pos["cost"] / pos["shares"]

    # ✅ Flexible price check (±10%)
    assert lower <= price_used <= upper, (
        f"Price {price_used} is outside allowed range ({lower}–{upper})"
    )

    # ✅ cash check
    expected_cash = 10000 - pos["cost"]
    assert abs(p.cash - expected_cash) < 1e-6

    print("✅ test_buy_stock passed (flexible pricing OK)")
