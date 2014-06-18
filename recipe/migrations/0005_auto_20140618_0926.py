# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_info_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='Ingredient3_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='info',
            name='Ingredient2_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='info',
            name='Ingredient4_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='info',
            name='Ingredient1_cost',
            field=models.IntegerField(default=0),
        ),
    ]
