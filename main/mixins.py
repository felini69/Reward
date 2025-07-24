from django.db import models
from django.utils.html import strip_tags
from tinymce.widgets import TinyMCE

class BaseModel(models.Model):
    """ Базовая модель для контейнеров """
    title = models.CharField(verbose_name='основной заголовок', max_length=1000)
    image = models.ImageField(verbose_name='изображение', upload_to='page_image')
    is_active = models.BooleanField(verbose_name='Активен', default=True)
    created_at = models.DateTimeField(verbose_name='Создано в', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено в', auto_now=True)

    class Meta:
        abstract = True


class BaseCards(models.Model):
    """ Базовая модель для карточек контейнеров """
    first_title = models.CharField(verbose_name='Первый заголовок', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=100, blank=True)
    is_active = models.BooleanField(verbose_name='Активен', default=True)
    created_at = models.DateTimeField(verbose_name='Создано в', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено в', auto_now=True)

    class Meta:
        abstract = True


class FormfieldesMixin:
    def strip_title(self, obj):
        return strip_tags(obj.title)
    strip_title.short_description = "заголовок" 

    formfield_overrides = {
        models.CharField: {'widget': TinyMCE()},
    }

    class Meta:
        abstract = True