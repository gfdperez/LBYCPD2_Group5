# Generated by Django 3.2 on 2021-05-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='item_ind',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
