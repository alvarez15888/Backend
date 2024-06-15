import requests

endpoint = 'http://localhost:8000/api_view/lost_found/lost/2/destroy'

res = requests.delete(endpoint)

print(res.status_code)