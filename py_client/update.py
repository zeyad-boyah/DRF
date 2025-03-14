import requests


endpoint = "http://localhost:8000/simple_api/products/1/update/"

data = {
    "title" : "this is mixin update",
    "price" : "69"
}
get_response = requests.put(endpoint, json= data )


print(get_response.json())
