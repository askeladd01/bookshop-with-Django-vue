# Generated by Django 3.2.5 on 2021-07-31 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20210729_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordergoods',
            name='real_price',
            field=models.FloatField(default=0.0, verbose_name='商品实价'),
        ),
    ]
