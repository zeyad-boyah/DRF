from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer

from django.shortcuts import get_object_or_404 


# Create your views here.
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # on by default but we can change it to title for example to make it work with the other commented view

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """
        basically I can use this hook to assign a product to the user who created it but 
        for now I am testing it
        """
        title = serializer.validated_data.get("title")
        description = serializer.validated_data.get("description") or None
        if description is None:
            description = title
        serializer.save(description=description)

@api_view(["GET", "POST"])
def alt_view_or_create_API(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if not pk == None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)