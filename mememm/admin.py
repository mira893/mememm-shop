from django.contrib import admin
from .models import Toy

@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'created_at')
    list_filter = ('available',)
    search_fields = ('name', 'description')

