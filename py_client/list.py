import requests


endpoint = "http://localhost:8000/simple_api/products/"


get_response = requests.get(endpoint)


print(get_response.json())
