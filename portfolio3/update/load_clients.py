import os
import json

CLIENTS_JSON_FILE = 'portfolio3/DATA/clients.json'

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

