from django.contrib import admin
from django.db import models
from unfold.admin import ModelAdmin
from .models import Logo, Favicon, Analytics, Terms
from tinymce.widgets import TinyMCE


@admin.register(Logo)
class LogoAdmin(ModelAdmin):
    list_display = ('title', 'created_at', 'is_active',)
    list_editable = ('is_active',)


@admin.register(Favicon)
class FaviconAdmin(ModelAdmin):
    list_display = ('created_at', 'is_active',)
    list_editable = ('is_active',)


@admin.register(Analytics)
class AnalyticsAdmin(ModelAdmin):
    list_display = ('name', 'created_at', 'is_active')
    list_editable = ('is_active', )


@admin.register(Terms)
class TermsAdmin(ModelAdmin):
    list_display = ('title', 'created_at', 'is_active',)
    list_editable = ('is_active',)

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
