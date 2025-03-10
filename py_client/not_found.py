import requests

endpoint = "http://localhost:8000/simple_api/products/10000000"


get_response = requests.get(endpoint, )


print(get_response.json())
