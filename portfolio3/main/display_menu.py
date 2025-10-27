
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