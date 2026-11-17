from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Ganr)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    


@admin.register(Video)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    
    
@admin.register(Comment)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')