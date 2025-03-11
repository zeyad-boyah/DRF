from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer



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

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 
    
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 

    def perform_destroy(self, instance):
        # todo add custom behavior
        return super().perform_destroy(instance)



"""
    an alt method to make the same functionality of create and list and detail with a function based view
"""
# from django.shortcuts import get_object_or_404 
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# @api_view(["GET", "POST"])
# def alt_view_or_create_API(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == "GET":
#         # retrieve a single object with pk 
#         if not pk == None:
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
#         # retrieve the whole thing
#         obj = Product.objects.all()
#         data = ProductSerializer(obj, many=True).data
#         return Response(data)
    
#     if method == "POST":
#         # create a new instance 
#         serializer = ProductSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= 201)
#         return Response({"invalid":serializer.errors}, status= 400)