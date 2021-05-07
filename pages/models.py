from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=20)
    subname = models.CharField(max_length=20)
    price_medium = models.IntegerField()
    price_large = models.IntegerField()
    image = models.ImageField(upload_to='menu')
    bgcolor = models.CharField(max_length=20)
    offer = models.BooleanField(default=False)
