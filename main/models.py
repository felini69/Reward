from django.db import models
from .mixins import BaseModel, BaseCards


class FirstContainer(BaseModel):
    """ Первый контейнер, наследуется от BaseModel """
    class Meta:
        verbose_name = "01 Главный контейнер"
        verbose_name_plural = "01 Главный контейнер"
        ordering = ['created_at']

    def __str__(self):
        return self.title



class SecondContainer(BaseModel):
    """ Второй контейнер, наследуется от BaseModel """
    class Meta:
        verbose_name = "02 Второй контейнер"
        verbose_name_plural = "02 Второй контейнер"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class SecondContainerCards(BaseCards):
    """ cards для второго контейнера """
    container = models.ForeignKey(SecondContainer, on_delete=models.SET_NULL, null=True, related_name='cards')
    second_title = models.CharField(verbose_name='Второй заголовок', max_length=100, blank=True)
    icon = models.ImageField(verbose_name='Иконка', upload_to='cards_icons/', blank=True, null=True)

    class Meta:
        verbose_name = "cards для второго контейнера"
        verbose_name_plural = "cards  для второго контейнера"
        ordering = ['-created_at']

    def __str__(self):
        return self.first_title


class ThirdContainer(BaseModel):
    """ Третий контейнер, наследуется от BaseModel """
    class Meta:
        verbose_name = "03 Третий контейнер"
        verbose_name_plural = "03 Третий контейнер"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    

class ThirdContainerCards(BaseCards):
    """ cards для третьего контейнера """
    container = models.ForeignKey(ThirdContainer, on_delete=models.SET_NULL, null=True, related_name='cards')


    class Meta:
        verbose_name = "cards для третьего контейнера"
        verbose_name_plural = "cards для третьего контейнера"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    

class FourthContainer(BaseModel):
    description = models.CharField(verbose_name='Описание', max_length=100)
    class Meta:
        verbose_name = "04 Четвертый контейнер"
        verbose_name_plural = "04 Четвертый контейнер"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    

class FourthContainerCards(BaseCards):
    container = models.ForeignKey(FourthContainer, verbose_name='Контейнер', on_delete=models.SET_NULL, null=True, related_name='cards')
    icon = models.ImageField(verbose_name='Иконка', upload_to='cards_icons/', blank=True, null=True)

    class Meta:
        verbose_name = "cards в четвертом контейнере"
        verbose_name_plural = "cards в четвертом контейнере"
        ordering = ['-created_at']

    def __str__(self):
        return self.first_title
    


class FivethContainer(BaseModel):
    """ Пятый контейнер, наследуется от BaseModel """
    class Meta:
        verbose_name = "05 Пятый контейнер"
        verbose_name_plural = "05 Пятый контейнер"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class FivethContainerCards(BaseCards):
    """ cards для пятого контейнера """
    container = models.ForeignKey(FivethContainer, verbose_name='Контейнер', on_delete=models.SET_NULL, null=True, related_name='cards')
    first_title = models.CharField(verbose_name='Заголовок', max_length=100)

    class Meta:
        verbose_name = "cards в пятом контейнере"
        verbose_name_plural = "cards в пятом контейнере"
        ordering = ['-created_at']

    def __str__(self):
        return self.first_title



class SixthContainer(BaseModel):
    """ Шестой контейнер, наследуется от BaseModel """
    description_1 = models.CharField(verbose_name='Описание 1', max_length=500)
    description_2 = models.CharField(verbose_name='Описание 2', max_length=500)
    class Meta:
        verbose_name = "06 Шестой контейнер"
        verbose_name_plural = "06 Шестой контейнер"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class SixthContainerCards(BaseCards):
    """ cards для шестого контейнера """
    container = models.ForeignKey(SixthContainer, verbose_name='Контейнер', on_delete=models.SET_NULL, null=True, related_name='cards')
    icon = models.ImageField(verbose_name='Иконка', upload_to='cards_icons/', blank=True, null=True)
    
    class Meta:
        verbose_name = "cards в шестом контейнере"
        verbose_name_plural = "cards в шестом контейнере"
        ordering = ['-created_at']

    def __str__(self):
        return self.first_title



class SeventhContainer(BaseModel):
    """ Седьмой контейнер, наследуется от BaseModel """
    description_1 = models.CharField(verbose_name='Описание 1', max_length=500)
    description_2 = models.CharField(verbose_name='Описание 2', max_length=500)
    class Meta:
        verbose_name = "07 Седьмой контейнер"
        verbose_name_plural = "07 Седьмой контейнер"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    
class SeventhContainerCards(models.Model):
    """ cards для седьмого контейнера """
    container = models.ForeignKey(SeventhContainer, verbose_name='Контейнер', on_delete=models.SET_NULL, null=True, related_name='cards')
    first_title = models.CharField(verbose_name='Заголовок', max_length=100)
    icon = models.ImageField(verbose_name='Иконка', upload_to='cards_icons/', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активен', default=True)
    created_at = models.DateTimeField(verbose_name='Создано в', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено в', auto_now=True)
    class Meta:
        verbose_name = "cards в седьмом контейнере"
        verbose_name_plural = "cards в седьмом контейнере"
        ordering = ['-created_at']

    def __str__(self):
        return self.first_title


class EighthContainer(BaseModel):
    """ Восьмой контейнер, наследуется от BaseModel """
    class Meta:
        verbose_name = "08 Восьмой контейнер"
        verbose_name_plural = "08 Восьмой контейнер"
        ordering = ['-created_at']

    def __str__(self):
        return self.title



class NinthContainer(BaseModel):
    """ Девятый контейнер наследуется от BaseModel """
    class Meta:
        verbose_name = "09 Девятый контейнер"
        verbose_name_plural = "09 Девятый контейнер"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class TenthContainer(BaseModel):
    """ Десятый контейнер наследуется от BaseModel """
    class Meta:
        verbose_name = "10 Десятый контейнер"
        verbose_name_plural = "10 Десятый контейнер"
        ordering = ['-created_at']

    def __str__(self):
        return self.title