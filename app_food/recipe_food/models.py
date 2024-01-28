from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    count_cooked = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MassProduct(models.Model):
    mass_product = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_id.name} ({self.mass_product} г.)'


class RecipeDish(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    mass_product_id = models.ManyToManyField(MassProduct)

    def __str__(self):
        return self.name

