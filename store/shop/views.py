from django.db import models
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProductListSerializer, ProductDetailSerializer
from .models import Product
from .services import ProductFilter


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
	"""Информация о продуктах"""
	filter_backends = (DjangoFilterBackend,)
	filterset_class = ProductFilter

	def get_queryset(self):
		products = Product.objects.all()
		return products
	def get_serializer_class(self):
		if self.action == 'list':
			return ProductListSerializer
		elif self.action == "retrieve":
			return ProductDetailSerializer
		