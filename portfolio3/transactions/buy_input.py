
from portfolio3.x_other.get_tickers import get_tickers
from portfolio3.update.create_transaction import create_transaction
def buy_input(active_client, clients):

    valid_tickers = get_tickers()

    current_cash = None    
    for position in active_client['positions']:
        if '$$$$' == position['symbol']:
            current_cash = position['shares']            
            break
    if not current_cash:
        print('FATAL ERROR: No cash position in positions (buy_inpt)')
        exit()

    CASH_BUFFER = 100.00

    txt = "enter the ticker you would like to buy: "
    while True:

        ticker = input(txt)

        if ticker == '': return None
        elif ticker not in valid_tickers:
            txt = 'Please enter a valid ticker: '
        else:
            name = valid_tickers[ticker]['full_name']
            print(name)
            break 

    
    txt = f'Please enter price of {ticker}: '
    while True:
        price = input(txt) 
        if ticker == '': return None

        try:
            price = float(price)
        except ValueError:
            txt = 'Please enter price: '
        else:
            if price <= 0:
                txt = 'Please enter a positive price: '
            else:
                break


    txt = 'How Many Shares would you like to buy? '
    
    while True:
        shares = input(txt)
        if shares == '': return None

        try:
            shares = int(shares)
            total_price = shares * price            
        except ValueError:
            txt = 'Please enter a positive integer: '
        else:
            if shares <= 0:
                txt = 'Pretty please, enter a positive integer: '
            elif total_price > (current_cash - CASH_BUFFER):
                txt = f"You don't have enough cash on hand to buy {shares}, enter lower amount: "
            else:
                break


    create_transaction(active_client['id'], 'BUY', shares, ticker, name, price, active_client, clients)    
    
    
    return