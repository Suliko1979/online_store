from django.db import models

from apps.products.models import Product
from apps.users.models import User


class Cart (models.Model):
    user = models.ForeignKey(to=User,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='user_cards')

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"{self.user.email} - cart: {self.id}"


class CartItem (models.Model):
    user = models.ForeignKey(to=Cart,
                             on_delete=models.CASCADE,
                             null=True,
                             related_name='cart_items')
    product = models.ForeignKey(to = Product,
                                on_delete=models.SET_NULL,
                                related_name='product_cart_item',
                                null=True)
    quantity = models.SmallIntegerField(verbose_name="Количество")


    class Meta:
        verbose_name = "Содержимое корзины"
        verbose_name_plural = "Содержимое корзины"

    def __str__(self):
        return f"Item: {self.id}, cart: {self.cart.id}"

