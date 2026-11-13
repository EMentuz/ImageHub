from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name # определяет, как объект модели  будет отображаться в виде текста

    class Meta:
        verbose_name = "Категория" #название модели в единственном числе.
        verbose_name_plural = "Категории" #название модели во множественном числе

class ImageModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    file = models.ImageField(upload_to='static/images/', verbose_name='Файл')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT,  verbose_name='Категория')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.user}'

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

# {% if image.author %}
#     {{ image.author.username }}
# {% else %}
#     Пользователь удалён
# {% endif %}
