import requests


endpoint = "http://localhost:8000/simple_api/products/"

data = {
    "title" : "the lost imposter",
    "description" : "hope he comes home",
    "price" : "69"
}
get_response = requests.post(endpoint, json= data )


print(get_response.json())
