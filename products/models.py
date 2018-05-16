from django.db import models
from django.template.defaultfilters import truncatechars
import PIL as pillow

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name  # отображение по имени

    class Meta:
        verbose_name = 'Количество комнат в квартире'
        verbose_name_plural = 'Количество комнат в квартирах'

class Product(models.Model):#поле для продукта

    name = models.CharField(max_length=128, blank=True, null=True, default=True)#имя для продукта
    # price = models.DecimalField(max_digits=10, decimal_places=2, default=True)  # поле для цена
    # discount = models.IntegerField(default=0)# поле для скидки
    # price_with_discount = models.DecimalField(max_digits=10, decimal_places=2, default=True)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=True)
    short_description = models.TextField(max_length=50, blank=True, null=True, default=None,)  # краткое описание для продукта
    description = models.TextField(blank=True, null=True, default=None)#описание для продукта
    is_active = models.BooleanField(default=True)#активность/неактивность проудкта
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)


    def description_S(self):
        return truncatechars(self.description, 30)
    def __str__(self):
            return "%s" % (self.name)#отображение по имени


    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'

class ProductImage(models.Model):#класс фотография
    Product = models.ForeignKey(Product, blank=True, null=True, default=None)#поле для продукта
    image = models.ImageField(upload_to='products_images/')#директория для фотографии продукта
    is_main = models.BooleanField(default=False)  # активность/неактивность товара
    is_active = models.BooleanField(default=True)#активность/неактивность товара
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
            return "%s" % (self.id)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'