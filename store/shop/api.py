from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Product
from .serializer import ProductListSerializer


class ProductList(viewsets.ViewSet):
	def list(self, request):
		queryset = Product.objects.all()
		serializer = ProductListSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrive(self, response, pk=None):
		queryset = Product.objects.all()
		product = get_object_or_404(queryset, pk=pk)
		serializer = ProductListSerializer(product)
		return Response(serializer.data)

