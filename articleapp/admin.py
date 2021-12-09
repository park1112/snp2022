from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    # prepopulated_fields = {'slug': ('name',)}


admin.site.register(Article, ArticleAdmin)


