
import json 

# def get_clients():
#     filename = 'clients.json'
#     data ='Ivan, 001, Maria, 002'

#     return [
#     {
#         'name': 'Ivan',
#         'pin': '0001'
     
#     },
#     {
#         'name': 'Maria',
#         'pin': '002'
#     }
# ]


filename = '.data/clients.json'
def get_clients():
    with open (filename, 'r') as f:
        client = json. load(f)
        return clients
    


def save_clients(clients):
   with open(filename, 'w') as f:
      json.dump(clients, f)
    #   to Json 


