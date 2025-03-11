from django.urls import path
from products import views


urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name="detail view with primary key"), 
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name="update a product with primary key"), 
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view(), name="delete a product with primary key"), 
    path('', views.ProductListCreateAPIView.as_view(), name="list all or Create a new instance of product"), 
]



# this is for testing the alt view
# from products.views import alt_view_or_create_API
# urlpatterns = [
#     path('<int:pk>/', view= alt_view_or_create_API, name="detail view with primary key"), 
#     path('', view=alt_view_or_create_API, name="list all or Create a new instance of product"), 
# ]


# this was to test str in the slug
# path('<str:title>/', ProductDetailAPIView.as_view(), name="detail view with title"), 