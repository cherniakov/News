from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name='Заголовок новости',
                             max_length=150)
    content = models.TextField(verbose_name='Текст', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновления',
                                      auto_now=True)
    photo = models.ImageField(verbose_name='Изображения',
                              upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(verbose_name='Публиковать',
                                       default=True)
    category = models.ForeignKey('Category', verbose_name='Категория',
                                 on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Категории")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title

