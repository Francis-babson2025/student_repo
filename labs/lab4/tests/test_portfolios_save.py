
from portfolios.portfolios import Portfolios

def test_portfolios_save_roundtrip(tmp_path):
    ps = Portfolios()
    a = ps.get_or_create_client("Alice")
    a.cash = 123.0
    a.positions = [{"sym":"AAPL","name":"Apple","shares":2,"cost":300.0}]
    fname = tmp_path / "clients.json"
    try:
        ps.save(str(fname))
    except NotImplementedError:
        assert False, "save() not implemented yet"
    ps2 = Portfolios().load(str(fname))
    assert "Alice" in ps2.clients
    a2 = ps2.clients["Alice"]
    assert a2.cash == 123.0
    assert a2.positions and a2.positions[0]["sym"] == "AAPL"
