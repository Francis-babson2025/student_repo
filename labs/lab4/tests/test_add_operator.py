
from portfolio import Portfolio

def test_add_operator_merges_positions_and_cash():
    p1 = Portfolio("A"); p1.cash = 100.0
    p1.positions = [{"sym":"AAPL","name":"Apple","shares":5,"cost":500.0}]
    p2 = Portfolio("B"); p2.cash = 200.0
    p2.positions = [{"sym":"AAPL","name":"Apple","shares":3,"cost":300.0},
                    {"sym":"MSFT","name":"Microsoft","shares":1,"cost":350.0}]
    try:
        r = p1 + p2
    except NotImplementedError:
        assert False, "__add__ not implemented yet"
    assert r.name == "A+B"
    assert r.cash == 300.0
    assert len(r.positions) == 2
    sym_to_pos = {pos["sym"]: pos for pos in r.positions}
    assert sym_to_pos["AAPL"]["shares"] == 8
    assert sym_to_pos["AAPL"]["cost"] == 800.0
    assert sym_to_pos["MSFT"]["shares"] == 1
