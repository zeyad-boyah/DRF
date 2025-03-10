from django.urls import path
from products.views import ProductDetailAPIView, ProductListCreateAPIView


urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view(), name="detail view with primary key"), 
    path('', ProductListCreateAPIView.as_view(), name="list all or Create a new instance of product"), 
]



# this is for testing the alt view
# from products.views import alt_view_or_create_API
# urlpatterns = [
#     path('<int:pk>/', view= alt_view_or_create_API, name="detail view with primary key"), 
#     path('', view=alt_view_or_create_API, name="list all or Create a new instance of product"), 
# ]


# this was to test str in the slug
# path('<str:title>/', ProductDetailAPIView.as_view(), name="detail view with title"), 