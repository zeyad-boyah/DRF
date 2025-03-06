import requests


"""
this is a simple client in python intended to test http response 
and using httpbin.org
"""
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint)

print(get_response.json())
# print(get_response.text)
# print(get_response.status_code)