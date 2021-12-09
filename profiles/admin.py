from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'nickname', 'message']
    # prepopulated_fields = {'slug': ('name',)}


admin.site.register(Profile, ProfileAdmin)


