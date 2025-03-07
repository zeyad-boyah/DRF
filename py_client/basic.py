import requests


"""
this is a simple client in python intended to test http response 
and using localhost
"""
# endpoint = "http://localhost:8000"
endpoint = "http://localhost:8000/simple_api/"


get_response = requests.get(endpoint, params={"abc":"123"}, json={"query":"hello from query"})

# print(get_response.json()['message'])
print(get_response.text)
# print(get_response.status_code)