import requests


# endpoint = "http://localhost:8000/simple_api/products/red%20Imposter"
endpoint = "http://localhost:8000/simple_api/products/1"


get_response = requests.get(endpoint, )

# print(get_response.json()['message'])
print(get_response.json())
# print(get_response.text)
# print(get_response.status_code)