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
    left = models.CharField(verbose_name='Левая часть', max_length=400, blank=True, null=True)
    right = models.CharField(verbose_name='Правая часть ', max_length=400, blank=True, null=True)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return f'Нижнее меню'