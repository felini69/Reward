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
    Logo,
    Favicon,
    
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



@admin.register(Logo)
class LogoAdmin(ModelAdmin, FormfieldesMixin):
    list_display = ('created_at', 'is_active',)
    list_editable = ('is_active',)



@admin.register(Favicon)
class FaviconAdmin(ModelAdmin, FormfieldesMixin):
    list_display = ('created_at', 'is_active',)
    list_editable = ('is_active',)























# class SecondContainerPostInlines(TabularInline):
#     model = SecondContainerPost
#     extra = 1
#     tab = True


# class tridContainerPostInlines(TabularInline):
#     model = tridContainerPost
#     extra = 1
#     tab = True


# # @admin.register(BaseContainer)
# # class BaseContainerAdmin(ModelAdmin):
# #     inlines = [SecondContainerPostInlines, tridContainerPostInlines]
    
# #     list_display = ('title', 'description_1', 'created_at',)
# #     formfield_overrides = {
# #         models.CharField: {'widget': TinyMCE(attrs={'cols': 5, 'rows': 2})},
# #     }

# #     def title(self, obj):
# #         return strip_tags(obj.title_1)


# @admin.register(BaseContainer)
# class BaseContainerAdmin(ModelAdmin):
#     # ----------------------------------------------------
#     # 1) Fieldsets become tabs by adding the "tab" CSS class
#     # ----------------------------------------------------
#     fieldsets = (
#         ((None), {
#             'fields': ('title_1', 'description_1', 'image_1'),
#         }),
#         (('Container 2'), {
#             'classes': ['tab'],       # <-- this fieldset is now “Tab 2”
#             'fields': ('title_2', 'image_2'),
#         }),
#         (('Container 3'), {
#             'classes': ['tab'],       # <-- “Tab 3” (no base fields here)
#             'fields': (),             
#         }),
#         (('Status & Dates'), {
#             'fields': ('is_active', ),
#         }),
#     )
#     # Unfold will detect those classes and render a little tab‐strip
#     # above the form content :contentReference[oaicite:2]{index=2}

#     # ----------------------------------------------------
#     # 2) Declare your inlines as usual…
#     # ----------------------------------------------------
#     inlines = [SecondContainerPostInlines, tridContainerPostInlines]

#     list_display = ('title', 'description_1', 'created_at')
#     formfield_overrides = {
#         models.CharField: {'widget': TinyMCE(attrs={'cols': 5, 'rows': 2})},
#     }

#     def title(self, obj):
#         return strip_tags(obj.title_1)




# # @admin.register(BaseContainer)
# # class BaseContainerAdmin(ModelAdmin):
# #     # указываем свой шаблон, он должен лежать в app/templates/admin/your_app/basecontainer/change_form.html
# #     # change_form_template = 'admin/main/basecontainer/change_form.html'

# #     fieldsets = (
# #         (('Первый контейнер'), {
# #             'classes': ['tab'],
# #             'fields': ('title_1', 'description_1', 'image_1'),
# #         }),
# #         (('Container 2'), {
# #             'classes': ['tab'],
# #             'fields': ('title_2', 'image_2'),
# #         }),
# #         (('Container 3'), {
# #             'classes': ['tab'],
# #             'fields': (),
# #         }),
# #         (('Status & Dates'), {
# #             # без 'tab' → остаётся в «General»
# #             'fields': ('is_active',),
# #         }),
# #     )
# #     inlines = [SecondContainerPostInlines, tridContainerPostInlines]

# #     list_display = ('title', 'description_1', 'created_at')
# #     formfield_overrides = {
# #         models.CharField: {'widget': TinyMCE(attrs={'cols': 5, 'rows': 2})},
# #     }

# #     def title(self, obj):
# #         return strip_tags(obj.title_1)




admin.site.unregister(Group)