
from portfolios.portfolios import Portfolios

def test_portfolios_load_sample_file():
    ps = Portfolios().load()
    assert "Alice" in ps.clients and "Bob" in ps.clients
    a = ps.clients["Alice"]
    assert isinstance(a.positions, list) and isinstance(a.cash, float)
