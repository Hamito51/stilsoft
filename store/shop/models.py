from django.db import models

# Create your models here.

class Subcategory(models.Model):
	"""Подкатегория"""
	name = models.CharField('Наименование', max_length=150)
	url = models.SlugField(max_length=160, unique=True)

	def __str__(seld):
		return self.name

	class Meta:
		verbose_name = 'Подкатегория'
		verbose_name_plural = 'Подкатегории'


class Category(models.Model):
	"""Категория"""
	name = models.CharField('Наименование', max_length=150)
	subcategory = models.ForeignKey(Subcategory, verbose_name='Подкатегория', on_delete=models.SET_NULL, null=True)
	url = models.SlugField(max_length=160, unique=True)

	def __str__(seld):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
			

class Products(models.Model):
	"""Товары"""
	name = models.CharField('Наименование', max_length=50)
	exp = models.PositiveSmallIntegerField('Срок годности', default=5)
	category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
	vendor_code = models.PositiveIntegerField('Артикул', default=1, unique=True)
	price = models.DecimalField('Цена', max_digits=6, decimal_places=2)
	subcategory = models.ForeignKey(Subcategory, verbose_name='Подкатегория', on_delete=models.SET_NULL, null=True)
	url = models.SlugField(max_length=160, unique=True)

	def __str__(seld):
		return self.name

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'
			