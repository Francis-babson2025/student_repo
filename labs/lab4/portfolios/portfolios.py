
from portfolio import Portfolio

class Portfolios:
    def __init__(self):
        self.clients = {}

    def get_or_create_client(self, name: str):
        print(self)
        if name in self.clients:
            return self.clients[name]
        p = Portfolio(name)
        self.clients[name] = p
        return p

    

    