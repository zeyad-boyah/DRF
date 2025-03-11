import requests

pk = input("please provide the primary key of the instance you want to delete: ")

try:
    pk = int(pk)
    endpoint = f"http://localhost:8000/simple_api/products/{pk}/delete/"
    get_response = requests.delete(endpoint)
    print(get_response.status_code)
except:
    print(f"{pk} is not a valid primary key")