from django.http import JsonResponse
from products.models import Product
import json

def api_home(request, *args, **kwargs):
    model_data =Product.objects.all().order_by("?").first() # get random instances of product 
    data = {}

    if model_data:
        data['title'] = model_data.title
        data['description'] = model_data.description
        data['price'] = model_data.price

    return JsonResponse(data)
