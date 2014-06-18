# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_remove_info_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
