# Generated by Django 3.2 on 2021-05-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='nameType',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='quanType',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='unitType',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
