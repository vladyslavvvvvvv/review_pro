from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=474),
    description = models.TextField(),
    price = models.DecimalField(decimal_places=1000,max_digits= 10000 )

    class Meta:
        verbose_name_plural = "products"

class Review(models.Model):
    text = models.TextField(),
    rating = models.IntegerField(),
    product = models.ForeignKey(Product, on_delete=models.CASCADE),
    author = models.CharField(max_length=474)

    class Meta: 
        verbose_name_plural = "reviewes"

