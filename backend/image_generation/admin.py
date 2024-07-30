from django.contrib import admin
from .models import Batch, Image

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    search_fields = ('id',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'image', 'batch')
    search_fields = ('prompt', 'batch__id')
    list_filter = ('batch',)
