# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipe_name', models.CharField(max_length=40)),
                ('cuisine_name', models.CharField(max_length=40)),
                ('Ingredient1_cost', models.IntegerField()),
                ('Ingredient2_cost', models.IntegerField()),
                ('Ingredient3_cost', models.IntegerField()),
                ('Ingredient4_cost', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
