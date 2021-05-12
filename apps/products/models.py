from django.db import models

from apps.users.models import User
from utils.uploads import upload_instance


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=250)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Picture(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to=upload_instance)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изобрадений'

    def __str__(self):
        return f'{self.id} - image'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products",
                                 verbose_name="Категория",
                                 null=True)
    pictures = models.ManyToManyField(to=Picture, related_name='product_pictures')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class Rating(models.Model):
    start = models.SmallIntegerField(verbose_name='Оценка товару')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE,
                                related_name='ratings')
    user = models.ForeignKey(to=User,
                             on_delete=models.SET_NULL,
                             related_name="user_ratings",
                             null=True)

    class Meta:
        verbose_name = 'Рейтинг товара'
        verbose_name_plural = 'Рейтинг товаров'

    def __str__(self):
        return f'Товар: {self.product.name}, рейтиг: {self.start}'


class Comments(models.Model):
    text = models.TextField(verbose_name="Отзыв")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE,
                                related_name='comments')
    user = models.ForeignKey(to=User,
                             on_delete=models.SET_NULL,
                             related_name="user_comments",
                             null=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Товар: {self.text[:100]}...'
