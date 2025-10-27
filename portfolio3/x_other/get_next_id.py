# ---------- Client Handling ----------
def get_next_id(clients):
    """Get the next available client ID."""
    next_id = max((client["id"] for client in clients), default=0) + 1

    #next_id = max([client["id"] for client in clients], default=0) + 1

    next_id = 0
    for client in clients:
        if client['id'] > next_id: next_id = client['id']
    next_id += 1

    return next_id