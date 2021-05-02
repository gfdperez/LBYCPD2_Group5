from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_add = models.EmailField(max_length=100)
    home_add = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=12)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
