from django.contrib import admin
from .models import Contact
from unfold.admin import ModelAdmin


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ('name', 'email', 'company', 'created_at')
    search_fields = ('name', 'email', 'company')
    ordering = ('-created_at',)