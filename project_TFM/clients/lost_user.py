import requests

endpoint = 'http://localhost:8000/api_view/lost_found/'

res = requests.get(endpoint)

print(res.json())