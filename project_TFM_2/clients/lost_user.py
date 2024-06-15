import requests
from getpass import getpass

endpoint = 'http://localhost:8000/auth/'
username = input('Usuario:')
password = getpass('Contraseña:')
token_res = requests.post(endpoint, json={'username':username, 'password':password})

print(token_res.json())
if token_res.status_code == 200:
    token = token_res.json()['token']
    headers = {
        "Authorization": f'Token {token}'
    }
    endpoint = 'http://localhost:8000/api_view/lost_found/lost/'

    res = requests.get(endpoint, headers=headers)

    print(res.json())