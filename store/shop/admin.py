from django.contrib import admin
from .models import Subcategory, Category, Products

# Register your models here.
@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_display_links = ('name',)


@admin.register(Category)
class SubcategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_display_links = ('name',)


@admin.register(Products)
class SubcategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'category', 'subcategory', 'vendor_code')
	list_display_links = ('name',)
	search_fields = ('name', 'category__name', 'subcategory__name')
