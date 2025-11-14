
from .base import Portfolio
from .init_method import portfolio_init
from .str_method import portfolio_str
from .add_cash import portfolio_add_cash
from .withdraw_cash import portfolio_withdraw_cash
from .buy_stock import portfolio_buy_stock
from .sell_stock import portfolio_sell_stock
from .view_last_close import portfolio_view_last_close
from .view_realtime import portfolio_view_realtime
from .add_operator import portfolio_add_operator

Portfolio.__init__ = portfolio_init
Portfolio.__str__ = portfolio_str
Portfolio.add_cash = portfolio_add_cash
Portfolio.withdraw_cash = portfolio_withdraw_cash
Portfolio.buy_stock = portfolio_buy_stock
Portfolio.sell_stock = portfolio_sell_stock
Portfolio.view_portfolio_last_close = portfolio_view_last_close
Portfolio.view_portfolio_realtime = portfolio_view_realtime
Portfolio.__add__ = portfolio_add_operator
