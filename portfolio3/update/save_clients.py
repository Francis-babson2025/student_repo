import json

CLIENTS_JSON_FILE = 'portfolio3/DATA/clients.json'

def save_clients(clients):
    """Save clients to JSON file."""    
    with open(CLIENTS_JSON_FILE, "w") as file:
        json.dump(clients, file, indent=4)
