import json


with open('login.json') as file:
    data = json.load(file)
    for client in data['user']:
        print(client['username'])
    