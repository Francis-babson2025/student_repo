from datetime import datetime 
from portfolio3.update._update_position import _update_position
from portfolio3.update.save_clients import save_clients

def create_transaction(next_id, type, shares,symbol, name, price, active_client, clients):

    
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

    _update_position(active_client, transaction)

    
    active_client['transactions'].append(transaction)
   
    save_clients(clients)
    return 