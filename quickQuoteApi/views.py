from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/cotizacion/', 
            'method': 'GET', 
            'body': None, 
            'description': 'Returns a list of products to select'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False )
    return Response(serializer.data)
