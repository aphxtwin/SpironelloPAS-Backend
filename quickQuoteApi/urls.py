from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('cotizacion/', views.get_products, name='productos'),
    path('cotizacion/<str:pk>/', views.get_product, name='producto')
]