from django.db import models
from rest_framework import viewsets
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
	"""Информация о продуктах"""
	def get_queryset(self):
		products = Product.objects.all()
		return products
	def get_serializer_class(self):
		if self.action == 'list':
			return ProductListSerializer
		elif self.action == "retrieve":
			return ProductDetailSerializer
		