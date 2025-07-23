from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    title = models.CharField(verbose_name='Название', max_length=100)
    container_id =models.PositiveSmallIntegerField(verbose_name='ID контейнера', default=1)
    order = models.PositiveIntegerField(default=0)
    parent = TreeForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='children',
        verbose_name='Parent'
        )
    is_active = models.BooleanField(default=True, verbose_name="Is Active")


    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
        ordering = ['order']

    def __str__(self):
        return self.title
    

class FooterMenu(models.Model):
    Left = models.CharField(verbose_name='Левая часть', max_length=400, blank=True, null=True)
    Right = models.CharField(verbose_name='Правая часть ', max_length=400, blank=True, null=True)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return f'Нижнее меню'
    


### Edditional class models for logo and ficon ###
class Logo(models.Model):
    """ Логотип сайта """
    title = models.CharField(verbose_name='Название', max_length=100, blank=True, null=True)
    image = models.ImageField(verbose_name='Логотип', upload_to='logo/')
    is_active = models.BooleanField(verbose_name='Активен', default=True)
    created_at = models.DateTimeField(verbose_name='Создано в', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено в', auto_now=True)

    class Meta:
        verbose_name = "Логотип"
        verbose_name_plural = "Логотипы"
        ordering = ['created_at']

    def __str__(self):
        return "Логотип сайта"
    

class Favicon(models.Model):
    """ Фавикон сайта """
    ficon = models.ImageField(verbose_name='Фавикон', upload_to='favicon/')
    is_active = models.BooleanField(verbose_name='Активен', default=True)
    created_at = models.DateTimeField(verbose_name='Создано в', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено в', auto_now=True)

    class Meta:
        verbose_name = "Фавикон"
        verbose_name_plural = "Фавиконы"

    def __str__(self):
        return "Фавикон сайта"