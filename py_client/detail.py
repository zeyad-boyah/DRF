import requests

pk = input("Please provide the primary key you want detailed view on: ")
try:
    pk = int(pk)
except:
    print(f"{pk} is not a valid primary key")

# endpoint = "http://localhost:8000/simple_api/products/red%20Imposter"
endpoint = f"http://localhost:8000/simple_api/products/{pk}"


get_response = requests.get(endpoint, )

# print(get_response.json()['message'])
print(get_response.json())
# print(get_response.text)
# print(get_response.status_code)