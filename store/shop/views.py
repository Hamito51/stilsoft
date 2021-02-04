from django.db import models
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import ProductListSerializer
from .serializers import ProductDetailSerializer
from .models import Product
from .services import ProductFilter
from .services import PaginationProduct


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
	"""Информация о продуктах"""
	# Настройки для фильтров и пагинации
	filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, )
	filterset_class = ProductFilter
	pagination_class = PaginationProduct
	search_fields = ('name', 'category__name', 'subcategory__name', 'vendor_code', )

	def get_queryset(self):
		products = Product.objects.all()
		return products
	def get_serializer_class(self):
		if self.action == 'list':
			return ProductListSerializer
		elif self.action == "retrieve":
			return ProductDetailSerializer
		