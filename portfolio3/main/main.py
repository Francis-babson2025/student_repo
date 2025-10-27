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

from portfolio3.update.load_clients import load_clients
from portfolio3.select.select_client import select_client
from portfolio3.select.input_client import input_client
from portfolio3.main.display_menu import display_menu
from portfolio3.transactions.buy_input import buy_input
from portfolio3.transactions.sell_input import sell_input
from portfolio3.transactions.contribution_input import contribution_input
from portfolio3.transactions.withdrawal_input import withdrawal_input
from portfolio3.x_other.view_portfolio import view_portfolio
from portfolio3.x_other.view_transactions import view_transactions


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
                                    buy_input(active_client,clients) 
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
