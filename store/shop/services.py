from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Product


class PaginationProduct(PageNumberPagination):
    """Настройки для пагинации"""
    page_size = 2
    max_page_size = 200

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
        

class ProductFilter(filters.FilterSet):
    """Регистронезависымые фильтры для товаров"""
    category = filters.CharFilter(field_name='category__name', lookup_expr='iexact')
    subcategory = filters.CharFilter(field_name='subcategory__name', lookup_expr='iexact')
    
    class Meta:
        model = Product
        fields = ['category', 'subcategory']