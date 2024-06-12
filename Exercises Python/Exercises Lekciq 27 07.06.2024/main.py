from db import get_clients, save_clients
# load data
clients = get_clients()

# clients.pop()

client = {
    'name' : 'Maria',
    'pin' : '002'
}

clients.append (clients)

save_clients(clients)