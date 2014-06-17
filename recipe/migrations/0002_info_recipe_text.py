# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='recipe_text',
            field=models.CharField(default=datetime.date(2014, 6, 17), max_length=500),
            preserve_default=False,
        ),
    ]
