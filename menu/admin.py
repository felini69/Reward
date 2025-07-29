from django.contrib import admin
from .models import MenuItem, FooterMenu
from .forms import MenuForm
from main.mixins import FormfieldesMixin
from unfold.admin import ModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin


@admin.register(MenuItem)
class MenuAdmin(DjangoMpttAdmin, ModelAdmin):
    form = MenuForm
    mptt_indent_field = "title"

    list_display = ('title', 'container_id', 'order', 'is_active')
    list_editable = ('is_active',)



@admin.register(FooterMenu)
class FooterMenuAdmin(ModelAdmin, FormfieldesMixin):
    formfield_overrides = FormfieldesMixin.formfield_overrides