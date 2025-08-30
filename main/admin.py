from django.contrib import admin
from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin, TabularInline
from django.db import models
from tinymce.widgets import TinyMCE
from .mixins import FormfieldesMixin
from .models import (
    FirstContainer,
    SecondContainer,
    SecondContainerCards,
    ThirdContainer,
    ThirdContainerCards,
    FourthContainer,
    FourthContainerCards,
    FivethContainer,
    FivethContainerCards,
    SixthContainer,
    SixthContainerCards,
    SeventhContainer,
    SeventhContainerCards,
    EighthContainer,
    NinthContainer,
    TenthContainer,
)


@admin.register(FirstContainer)
class FirstContainerAdmin(ModelAdmin, FormfieldesMixin):
    list_display = ('strip_title', 'created_at', 'is_active',)
    list_editable = ('is_active',)

    formfield_overrides = FormfieldesMixin.formfield_overrides



class SecondContainerCardInlines(TabularInline):
    model = SecondContainerCards
    extra = 1
    """ используйте это для упорядочивания полей в панели администратора """
    fields = (
        'first_title',
        'second_title',
        'description',
        'icon',
        'is_active',
    )

@admin.register(SecondContainer)
class SecondContainerAdmin(ModelAdmin, FormfieldesMixin):
    inlines = [SecondContainerCardInlines]

    list_display = ('strip_title', 'created_at', 'is_active',)
    list_editable = ('is_active',)

    formfield_overrides = FormfieldesMixin.formfield_overrides



class ThirdContainerCardsInlines(TabularInline):
    model = ThirdContainerCards
    extra = 1


@admin.register(ThirdContainer)
class ThirdContainerAdmin(ModelAdmin, FormfieldesMixin):
    inlines = [ThirdContainerCardsInlines]

    list_display = ('strip_title', 'created_at', 'is_active',)
    list_editable = ('is_active',)

    formfield_overrides = FormfieldesMixin.formfield_overrides
    


class FourthContainerCardsInlines(TabularInline):
    model = FourthContainerCards
    extra = 1
    fields = (
        'first_title',
        'icon',
        'is_active',
    )


@admin.register(FourthContainer)
class FourthContainerAdmin(ModelAdmin, FormfieldesMixin):
    inlines = [FourthContainerCardsInlines]

    list_display = ('strip_title', 'created_at', 'is_active',)
    list_editable = ('is_active',)
    fields = (
        'title',
        'description',
        'image',
        'is_active',
    )

    formfield_overrides = FormfieldesMixin.formfield_overrides


class FivethContainerCardsInlines(TabularInline):
    model = FivethContainerCards
    extra = 1
    fields = (
        'first_title',
        'description',
        'is_active',
    )


@admin.register(FivethContainer)
class FivethContainerAdmin(ModelAdmin, FormfieldesMixin):
    inlines = [FivethContainerCardsInlines]

    list_display = ('strip_title', 'created_at', 'is_active',)
    list_editable = ('is_active',)

    formfield_overrides = FormfieldesMixin.formfield_overrides


class SixthContainerCardsInlines(TabularInline):
    model = SixthContainerCards
    extra = 1
    fields = (
        'first_title',
        'icon',
    )


@admin.register(SixthContainer)
class SixthContainerAdmin(ModelAdmin, FormfieldesMixin):
    inlines = [SixthContainerCardsInlines]

    list_display = ('strip_title', 'created_at', 'is_active',)
    list_editable = ('is_active',)

    formfield_overrides = FormfieldesMixin.formfield_overrides



class SeventhContainerCardsInlines(TabularInline):
    model = SeventhContainerCards
    extra = 1
    fields = (
        'first_title',
        'icon',
    )


@admin.register(SeventhContainer)
class SeventhContainerAdmin(ModelAdmin, FormfieldesMixin):
    inlines = [SeventhContainerCardsInlines]

    list_display = ('strip_title', 'created_at', 'is_active',)
    list_editable = ('is_active',)
    fields = (
        'title',
        'description_1',
        'description_2',
        'image',
        'is_active',
    )

    formfield_overrides = FormfieldesMixin.formfield_overrides



@admin.register(EighthContainer)
class EighthContainerAdmin(ModelAdmin, FormfieldesMixin):
    list_display = ('strip_title', 'created_at', 'is_active',)
    list_editable = ('is_active',)

    formfield_overrides = FormfieldesMixin.formfield_overrides



@admin.register(NinthContainer)
class NinthContainerAdmin(ModelAdmin, FormfieldesMixin):
    list_display = ('strip_title', 'created_at', 'is_active',)
    list_editable = ('is_active',)

    formfield_overrides = FormfieldesMixin.formfield_overrides



@admin.register(TenthContainer)
class TenthContainerAdmin(ModelAdmin, FormfieldesMixin):
    list_display = ('strip_title', 'created_at', 'is_active',)
    list_editable = ('is_active',)

    formfield_overrides = FormfieldesMixin.formfield_overrides

