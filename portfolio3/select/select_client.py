from portfolio3.main.display_menu import display_menu

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