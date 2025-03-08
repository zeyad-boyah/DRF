from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
import json


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data =Product.objects.all().order_by("?").first() # get random instances of product 
    data = {}

    if model_data:
        serialized_data = ProductSerializer(model_data).data
        return Response(serialized_data)





    # if model_data:
    #    data = model_to_dict(model_data)
    # return JsonResponse(data)
