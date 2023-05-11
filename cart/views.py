from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from cart.models import Cart, CartProduct
from cart.serializer import CartSerializer, CartProductSerializer, CartProductUpdateSerializer
from product.models import Product


class CartView(APIView):

    @api_view(['GET'])
    def get_all(request):
        checkouts = CartProduct.objects.all()
        serializer = CartProductSerializer(checkouts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(method='post', request_body=CartProductSerializer)
    @api_view(['Post'])
    def create_checkout(request):
        serializer = CartProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(method='put', request_body=CartProductUpdateSerializer)
    @api_view(['PUT'])
    def update_checkout(request, id):
        checkout = get_object_or_404(CartProduct, pk=id)
        """serializer = CartProductSerializer(checkout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)"""
        checkout.quantity = request.data['quantity']
        serializer = CartProductSerializer(data=checkout)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.data, status=status.HTTP_200_OK)