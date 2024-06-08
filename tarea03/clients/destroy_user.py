import requests

endpoint = 'http://localhost:8000/api_view/caluladora/1/destroy'

res = requests.delete(endpoint)

print(res.status_code)