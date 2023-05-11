from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from product.models import Product
from product.serializer import ProductSerializer


class ProductView(APIView):

    @api_view(['GET'])
    def get_all(request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def get_by_name(request, name: str):
        product = get_object_or_404(Product, name__icontains=name)
        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(method='post', request_body=ProductSerializer)
    @api_view(['POST'])
    def create_product(request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(method='put', request_body=ProductSerializer)
    @api_view(['PUT'])
    def update_product(request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    def delete_product(request, id):
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)