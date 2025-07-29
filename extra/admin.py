from django.contrib import admin
from unfold.admin import ModelAdmin
from main.mixins import FormfieldesMixin
from .models import Logo, Favicon, Analytics


@admin.register(Logo)
class LogoAdmin(ModelAdmin, FormfieldesMixin):
    list_display = ('title', 'created_at', 'is_active',)
    list_editable = ('is_active',)



@admin.register(Favicon)
class FaviconAdmin(ModelAdmin, FormfieldesMixin):
    list_display = ('created_at', 'is_active',)
    list_editable = ('is_active',)


@admin.register(Analytics)
class AnalyticsAdmin(ModelAdmin):
    list_display = ('name', 'created_at', 'is_active')
    list_editable = ('is_active', )