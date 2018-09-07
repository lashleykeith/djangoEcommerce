# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, related_name='orders', to='coupons.Coupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(verbose_name='address', max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(verbose_name='city', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(verbose_name='e-mail', max_length=254),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(verbose_name='first name', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(verbose_name='last name', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(verbose_name='postal code', max_length=20),
        ),
    ]
