
import os, time, datetime
import prices
from portfolios.portfolios import Portfolios

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()

def print_portfolio_table_from_map(portfolio, px_map):    
    # Header
    print(f"{'Shares':<12}{'Symbol':<12}{'CPS':<12}{'Price':<12}{'MKT':<12}")
    print("-" * 60)

    for pos in portfolio.positions:
        sym = pos["sym"]
        shares = pos["shares"]
        cost = pos["cost"]
        price = px_map.get(sym, float("nan"))
        avg_cost = (cost / shares) if shares > 0 else float("nan")
        mv = price if price == price else float("nan")

        print(f"{shares:<12,.0f}"
              f"{sym:<12}"
              f"{avg_cost:<12,.2f}"
              f"{price:<12,.2f}"
              f"{mv:<12,.2f}")


def manage_portfolio(portfolio):
    while True:
        clear_screen()
        print(f"=== {portfolio.name}'s Portfolio ===")
        print("1. View portfolio (last night’s close)")
        print("2. View portfolio (real-time prices)")
        print("3. Buy stock")
        print("4. Sell stock")
        print("5. Add cash")
        print("6. Withdraw cash")
        choice = input("Enter choice (or press Enter to return): ").strip()
        if not choice:
            return
        if choice == "1":
            clear_screen()
            try:
                px_map = portfolio.view_portfolio_last_close()   # returns dict
                print_portfolio_table_from_map(portfolio, px_map)
            except NotImplementedError as e:
                print(e)
            input("\n(Press Enter to return)")

        elif choice == "2":
            if not prices.market_is_open():
                clear_screen()
                print("Market is closed. Showing last-night close instead:\n")
                try:
                    px_map = portfolio.view_portfolio_last_close()
                    print_portfolio_table_from_map(portfolio, px_map)
                except NotImplementedError as e:
                    print(e)
                input("\n(Press Enter to return)")
            else:
                # live loop
                try:
                    import msvcrt
                    is_win = True
                except Exception:
                    is_win = False

                try:
                    while True:
                        clear_screen()
                        ts = datetime.datetime.now().strftime("%H:%M:%S")
                        print("-"*60)
                        print(f" Real-Time Portfolio Prices (updated {ts})")
                        print("-"*60)
                        try:
                            px_map = portfolio.view_portfolio_realtime()   # returns dict
                            print_portfolio_table_from_map(portfolio, px_map)
                        except NotImplementedError as e:
                            print(e)
                            input("\n(Press Enter to return)")
                            break

                        print("\n(Press Enter to return to the previous menu)")
                        for _ in range(50):  # ~5 seconds total
                            if is_win:
                                import msvcrt
                                if msvcrt.kbhit() and msvcrt.getwch() == "\r":
                                    raise KeyboardInterrupt
                            time.sleep(0.1)
                except KeyboardInterrupt:
                    pass

        elif choice == "3":
            sym = input("Symbol (Enter to cancel): ").upper().strip()
            if not sym:
                continue
            px = prices.get_live_map([sym]).get(sym)
            clear_screen()
            if px is None or px != px:
                print("Price unavailable."); input("\n(Press Enter to return)"); continue
            print(f"{sym} is currently trading at ${px:,.2f}")
            s = input("How many shares would you like to buy? (Enter to cancel): ").strip()
            if not s:
                continue
            try:
                shares = float(s)
                portfolio.buy_stock(sym, shares, px)
                print("Your purchase is confirmed.")
            except Exception as e:
                print(e)
            input("\n(Press Enter to return)")
        elif choice == "4":
            sym = input("Symbol (Enter to cancel): ").upper().strip()
            if not sym:
                continue
            px = prices.get_live_map([sym]).get(sym)
            clear_screen()
            if px is None or px != px:
                print("Price unavailable."); input("\n(Press Enter to return)"); continue
            print(f"{sym} is currently trading at ${px:,.2f}")
            s = input("How many shares would you like to sell? (Enter to cancel): ").strip()
            if not s:
                continue
            try:
                shares = float(s)
                portfolio.sell_stock(sym, shares, px)
                print("Sell submitted.")
            except Exception as e:
                print(e)
            input("\n(Press Enter to return)")
        elif choice == "5":
            s = input("Amount to add (Enter to cancel): ").strip()
            if not s:
                continue
            try:
                portfolio.add_cash(float(s))
                print("Cash added.")
            except Exception as e:
                print(e)
            input("\n(Press Enter to return)")
        elif choice == "6":
            s = input("Amount to withdraw (Enter to cancel): ").strip()
    
            if not s:
                continue
            try:
                portfolio.withdraw_cash(float(s))
                print("Cash withdrawn.")
            except Exception as e:
                print(e)
            input("\n(Press Enter to return)")

def main():
    #clear_screen()
    ps = Portfolios().load()
    
    while True:
        #clear_screen()
        print("=== Main Menu ===")
        print("1. Select existing client")
        print("2. Create new client")
        choice = input("Enter choice (or press Enter to exit): ").strip()
        if not choice:
            try:
                ps.save()
                print("Saved.")
            except Exception:
                pass
            print("Goodbye!")
            break
        if choice == "1":
            name = input("Client name (Enter to cancel): ").strip()
            if not name:
                continue    
            
            time.sleep(5)
            if name in ps.clients:
                manage_portfolio(ps.clients[name])
            else:
                print("Client not found."); time.sleep(1)
        elif choice == "2":
            name = input("New client name (Enter to cancel): ").strip()
            if not name:
                continue
            p = ps.get_or_create_client(name)
            manage_portfolio(p)

if __name__ == "__main__":
    main()
