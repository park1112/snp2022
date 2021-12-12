from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ProductType, ProductTypeAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available_display', 'available_order', 'created', 'updated']
    list_filter = ['available_display', 'created', 'updated', 'category']
    prepopulated_fields = {'slug': ('name',)}   #이름을 쓰면 슬로그에 자동으로 등록된다 .
    list_editable = ['price', 'stock', 'available_display', 'available_order']  #자주 바뀌는거 등록해놈 바로바뀔수 있게


admin.site.register(Product, ProductAdmin)
