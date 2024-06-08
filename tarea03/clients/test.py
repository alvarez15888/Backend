import requests

endpoint = 'http://localhost:8000/api_view/'

get_response = requests.get(endpoint,json={'cuerpo': 'hola que tal'})

print(get_response.json())