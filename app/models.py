from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='banners/', verbose_name='Изображение')

    def __str__(self):
        return self.title
