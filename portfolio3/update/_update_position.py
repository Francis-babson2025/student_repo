def _update_position(active_client, transaction):
    # helper function to only be used inside create_transaction       

    # Short local aliases for readability
    txn_type = transaction['type']
    txn_symbol = transaction['symbol']
    txn_shares = transaction['shares']
    txn_price = transaction.get('trn_price')  # price may be used for cost calculations

    if txn_type == 'CONTRIBUTION':
        # If client already has any positions, try to find the matching one and add shares.
        if active_client['positions']:
            for pos in active_client['positions']:
                if pos['symbol'] == txn_symbol:
                    # Add contributed shares to the existing position (no avg_cost change here)
                    pos['shares'] += txn_shares
        else:
            # No positions at all: create a new position record for this contribution
            new_position = {
                'id': transaction['id'],
                'shares': round(txn_shares, 2),
                'symbol': txn_symbol,
                'name': transaction['name'],
                'avg_cost': txn_price
            }
            active_client['positions'].append(new_position)    

    elif txn_type == 'BUY':
        # Find an existing position with the same symbol (if any)
        matched_position = None
        for pos in active_client['positions']:
            if txn_symbol == pos['symbol']:
                matched_position = pos
                break

        if matched_position:
            # Update weighted average cost when adding shares to an existing position
            '''
            the total cost of our old position is just the number of shares we hold * the avg_cost
            call this old_total_cost.

            our new_total_cost = old_total_cot + txn_shares + txn_price
            new_avg_cost = new_total_cost / (matched_position['shares'] + txn_shares)  
            '''

            old_total_cost = matched_position['shares'] * matched_position['avg_cost']
            new_total_cost = old_total_cost + txn_shares * txn_price

            matched_position['shares'] += txn_shares  
            matched_position['avg_cost'] = new_total_cost / matched_position['shares']

        else:
            # No existing position: create a new one with the buy transaction values
            new_position = {
                'id': transaction['id'],
                'shares': round(txn_shares, 2),
                'symbol': txn_symbol,
                'name': transaction['name'],
                'avg_cost': txn_price
            }
            active_client['positions'].append(new_position)

        # Adjust the special cash placeholder position '$$$$' by deducting the cash spent.
        # NOTE: this subtracts dollar value (shares * price) from the cash "shares" field.
        # That is, the '$$$$' position tracks cash in the same 'shares' field.
        for pos in active_client['positions']:
            if '$$$$' == pos['symbol']:
                pos['shares'] -= (txn_shares * txn_price)

    elif txn_type == 'SELL':
        pass
    elif txn_type == 'WITHDRAWAL':
        pass
    else:
        print('FATAL ERROR: we should never get here _update_position')
        exit()
    return