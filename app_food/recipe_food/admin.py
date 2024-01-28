from django.contrib import admin
from . import  models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'count_cooked', 'date_created']
    list_display_links = ['id']


@admin.register(models.MassProduct)
class MassProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'mass_product', 'product_id']
    list_display_links = ['id']


@admin.register(models.RecipeDish)
class RecipeDishAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_created']
    list_display_links = ['id']


