import os
def clear_screen():
    
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS / Linux
    else:
        os.system('clear')

    print(os.name)