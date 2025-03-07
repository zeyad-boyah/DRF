from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.models import Product
import json

def api_home(request, *args, **kwargs):
    model_data =Product.objects.all().order_by("?").first() # get random instances of product 
    data = {}

    if model_data:
        data = model_to_dict(model_data)
    return JsonResponse(data)
