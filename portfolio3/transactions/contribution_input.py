from portfolio3.update.create_transaction import create_transaction

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
      
    
    create_transaction(active_client['id'], 'CONTRIBUTION', shares, '$$$$', 'Cash', 1.00, active_client, clients)    
    
    
    return