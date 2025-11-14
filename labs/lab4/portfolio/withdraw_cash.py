import time
def portfolio_withdraw_cash(self, amount: float):
    """TODO:
    - Reject negative
    - Reject if amount > cash
    - Otherwise subtract from self.cash
    """
    if amount < 0:
        print("You can not withdraw negative ")
        time.sleep(1)
        
    elif amount > self.cash:
        print(f"you only have ${self.cash:,.2f}, sell some stock first!")
        time.sleep(1)
        
    else:
        self.cash -= amount
        print(f"Your check for 4{amount:,.2f} is in the mail")
        time.sleep(1)

    return None
        