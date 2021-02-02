from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = format_suffix_patterns([
	path('product/', views.ProductViewSet.as_view({'get': 'list'})),
	path('product/<int:pk>/', views.ProductViewSet.as_view({'get': 'retrieve'})),
])