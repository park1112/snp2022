from django.contrib import admin
from .models import *


class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Expertise, ExpertiseAdmin)


class CompanyNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(CompanyName, CompanyNameAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'expertise', 'companyname', 'phone_number', 'available_display', 'available_order', 'created', 'updated']
    list_filter = ['available_display', 'created', 'updated', 'expertise']
    prepopulated_fields = {'slug': ('name',)}   #이름을 쓰면 슬로그에 자동으로 등록된다 .
    list_editable = ['phone_number', 'available_display', 'available_order']  #자주 바뀌는거 등록해놈 바로바뀔수 있게


admin.site.register(Client, ClientAdmin)