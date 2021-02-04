from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.FilterSet):
	"""Регистронезависымые фильтры для товаров"""
	category = filters.CharFilter(field_name='category__name', lookup_expr='iexact')
	subcategory = filters.CharFilter(field_name='subcategory__name', lookup_expr='iexact')
	
	class Meta:
		model = Product
		fields = ['category', 'subcategory']