'''
    clients = []                        clients is just a list


    client = {'id':None,                client is just a dictionary
              'fname': None,
              'lname': None,              
              'positions': [],          but it also contains two lists
              'transactions': []}
    
    position = {'id': None,             position is just a dictionary
                'shares': None,         integer except for cash
                'symbol': None,         sp500 + $$$$
                'name': None,
                'avg_cost':None}
    
    transaction ={'id': None,           transaction is just a dictionary
                  'timestamp': None,   
                  'type': None,         BUY, SELL, CONTRIBUTION, WITHDRAWAL
                  'shares': None,       integer except for cash
                  'symbol': None,       sp500 + $$$$
                  'name': None,
                  'trn_price': None}

what do clients, positions and transactions contain? 

what design issues are we not handling?

How do we store our data?
'''


import json
import os
import csv
from datetime import datetime 
from decimal import Decimal, ROUND_HALF_UP

CLIENTS_JSON_FILE = 'portfolio/clients.json'

# ---------- File Handling ----------
def load_clients():
    """Load clients from JSON file or return empty list."""
    if os.path.exists(CLIENTS_JSON_FILE):
        try:
            with open(CLIENTS_JSON_FILE, 'r') as file:                
                return json.load(file)
        except json.JSONDecodeError:
            print('FATAL ERROR: Your clients.json file is corrupt 000')
            exit()
    return []



def save_clients(clients):
    """Save clients to JSON file."""
    #print(CLIENTS_JSON_FILE)
    with open(CLIENTS_JSON_FILE, "w") as file:
        json.dump(clients, file, indent=4)





# ---------- Client Handling ----------
def get_next_id(clients):
    """Get the next available client ID."""
    next_id = max((client["id"] for client in clients), default=0) + 1

    #next_id = max([client["id"] for client in clients], default=0) + 1

    next_id = 0
    for client in clients:
        if client['id'] > next_id: next_id = client['id']
    next_id += 1

    return next_id


def _update_position(client, transaction):
    # helper function to only be used inside create_transaction

    active_positions = client['positions']

    if transaction['type'] == 'CONTRIBUTION':
        if active_positions:
            for position in active_positions:                
                if position['symbol'] == transaction['symbol']:
                    position['shares'] += transaction['shares']
        else:
            position = {'id': transaction['id'],            
            'shares': round(transaction['shares'], 2),
            'symbol': transaction['symbol'],
            'name': transaction['name'],
            'avg_cost': transaction['trn_price']}

            active_positions.append(position)    # or client['positions].append(position)

    return


def create_transaction(next_id, type, shares,symbol, name, price, client):

    
    """Create a cash contribution transaction."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    transaction =  {
        'id': next_id,
        'timestamp': timestamp,
        'type': type,
        'shares': round(shares, 2) if type in ('CONTRIBUTION', 'WITHDRAWAL')  else shares,
        'symbol': symbol,
        'name': name,
        'trn_price': round(price, 2)
    }

    _update_position(client, transaction)

    
    client['transactions'].append(transaction)
   

    return 




def input_client(clients):
    """Gather client input (name + cash) and add to clients list."""
    fname = input('Please enter your first name: ')
    lname = input('Please enter your last name: ')

    if not fname or not lname:
        return None  # go back to menu    
    

    next_id = get_next_id(clients)

    client = {
        'id': next_id,
        'fname': fname,
        'lname': lname,
        'positions': [],
        'transactions': []
    }

    clients.append(client)
    contribution_input(client, clients)

    return 
   

    
def select_client(clients):


    if not clients:
        print('You have no clients, please create 1 first before selecting (select_client())')
        return None

    menu_items = []
    for client in clients:        
        name = client['fname'] + ' ' + client['lname']
        menu_items.append(name)
       
    while True:
        choice = display_menu(menu_items)
        if choice == None:                
            return None                
        else:
            #what does choice contain here? what are we returning?                
            return clients[choice - 1] 

# ---------- Menu Handling ----------
def display_menu(menu_items):
    """Display a menu and return a valid integer choice."""
    txt = 'Select menu item (display_menu()): '
    while True:
        print('\n\n\n')
        for idx, item in enumerate(menu_items, start=1):
            print(f'{idx}) {item}')
        print('\n\n')

        item_no = input(txt)
        try:
            item_no = int(item_no)
        except ValueError:
            if item_no == '':                               
                return None
            txt = 'Please select an integer item (display_menu()): '
        else:
            if 1 <= item_no <= len(menu_items):
                return item_no
            else:
                txt = f'Enter an integer between 1 and {len(menu_items)} (display_menu()): '

def buy_input(active_client):
    print('get some input from user')
    print('if user finishes or enters "" return')

def sell_input(active_client):
    print('get some input from user')
    print('if user finishes or enters "" return')

def contribution_input(active_client, clients):

    txt = 'How much cash would you like to contribute? '    
    
    while True:
        shares = input(txt)
        if shares == '': return

        try:
            shares = float(shares)
        except ValueError:
            txt = 'Please enter a dollar amount: '
        else:
            if shares <= 0:
                txt = 'Please input a positive amount: '
            else:
                break
      
    
    create_transaction(active_client['id'], 'CONTRIBUTION', shares, '$$$$', 'Cash', 1.00, active_client)    
    save_clients(clients)
    
    return







    print('get some input from user')
    print('if user finishes or enters "" return')
def withdrawal_input(active_client):
    print('get some input from user')
    print('if user finishes or enters "" return')

def view_portfolio(active_client):
    print('show portfolio')
    print('when user enters "" return')
def view_transactions(active_client):
    print('show portfolio')
    print('when user enters "" return')

import csv
from pprint import pprint
def get_tickers():
    tickers = {}

    with open("portfolio/ticker.data", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:            
            ticker = row["Ticker"]
            tickers[ticker] = {
                "short_name": row["Short Name"],
                "full_name": row["Full Corporate Name"]
            }

    pprint(tickers)
    print(tickers['TSLA'])
    print(tickers['TSLA']['short_name'])
    return tickers

#get_tickers()


# ---------- Main Flow ----------
def main():
    clients = load_clients()   
    
    while True:
        s0_menu_items = ('Select client', 'Create client')
        choice = display_menu(s0_menu_items)

        if choice == None:
            print('exit system s0')
            exit()
        
        elif choice == 1:            
            while True:                
                choice = select_client(clients)                       
                if choice == None:
                    print('return to previous menu s00 -> s0')
                    break
                else:
                    active_client = choice
                    while True:
                        s1_menu_items =('Transactions', 'View Portfolio', 'View Transactions')
                        choice = display_menu(s1_menu_items)
                        if choice == None:
                            print('return to previous menu s1 -> s00')
                            break
                        elif choice == 1:
                            while True:
                                s10_menu_items =('Buy', 'Sell', 'Contribution', 'Withdrawal')
                                choice = display_menu(s10_menu_items)
                                if choice == None:
                                    print('return to previous menu s10 -> s1')
                                    break
                                elif choice == 1:
                                    '''
                                    get buy input, wait for return to break out of loop
                                    '''   
                                    buy_input(active_client) 
                                    break                                
                                elif choice == 2:
                                    '''
                                    get sell input, wait for return to break out of loop
                                    '''
                                    sell_input(active_client) 
                                    break     
                                elif choice == 3:
                                    '''
                                    get contribution input, wait for return to break out of loop
                                    '''
                                    contribution_input(active_client, clients) 
                                    break     
                                elif choice == 4:
                                    '''
                                    get withdrawal input, wait for return to break out of loop
                                    '''
                                    withdrawal_input(active_client) 
                                    break     
                                else:
                                    print('FATAL ERROR: we should never get here s10 bad input')

                            
                        elif choice == 2:
                            '''
                            view portfolio
                            wait for None return to break out of loop
                            '''
                            view_portfolio(active_client)
                            break
                        elif choice == 3:
                            '''
                            view transactions
                            wait for None return  to break out of loop
                            '''
                            view_transactions()
                            break
                        else:
                            print("FATAL ERROR: should never get here s1 bad input")

                        
                        

        elif choice == 2:  # Create client
            while True:
                choice = input_client(clients)
                if choice == None:
                    print('return to previous menu s01 -> s0')
                    break
                else:
                    new_client = choice
                    print(f"Client {new_client['fname']} {new_client['lname']} created. s01 -> s0")
                    break  # break out of loop  go to s0
        else:
            print("FATAL ERROR: should never get here s0 bad input")
        


if __name__ == "__main__":
    main()
