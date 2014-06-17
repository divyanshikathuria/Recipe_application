# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_info_recipe_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='Ingredient1',
            field=models.CharField(default=datetime.date(2014, 6, 17), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='Ingredient2',
            field=models.CharField(default=datetime.date(2014, 6, 17), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='Ingredient3',
            field=models.CharField(default=datetime.date(2014, 6, 17), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='Ingredient4',
            field=models.CharField(default=datetime.date(2014, 6, 17), max_length=30),
            preserve_default=False,
        ),
    ]
