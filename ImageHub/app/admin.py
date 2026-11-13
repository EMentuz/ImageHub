from django.contrib import admin
from .models import CategoryModel, ImageModel

# Register your models here.


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'update_at')
    search_fields = ['name']

@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'user', 'created_at', 'updated_at', 'is_active')
    search_fields = ['name']


