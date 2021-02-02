from rest_framework import serializers
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
	"""Список продуктов"""
	class Meta:
		model = Product
		fields = ('name', 'category', 'price')
			

class ProductDetailSerializer(serializers.ModelSerializer):
	"""Информация о продукте"""
	class Meta:
		model = Product
		exclude = ('url',)