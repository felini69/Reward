from django.db import models

### Дополнительные модели классов для логотипа и значка ###
class Logo(models.Model):
    """ Логотип сайта """
    title = models.CharField(verbose_name='Название', max_length=100, blank=True, null=True)
    POSITION_CHOICES = (
        ('header', 'Header'),
        ('footer', 'Footer'),
    )
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, blank=True)
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
    


### Дополнительная модель класса для аналитики ###
class Analytics(models.Model):
    name = models.CharField(verbose_name='Название аналитика', max_length=50)
    analytic = models.TextField(
        verbose_name='Код аналитики', 
        help_text='Вставьте сюда весь скрипт, чтобы включить аналитику на сайте.',
        max_length=500 )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Terms(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title