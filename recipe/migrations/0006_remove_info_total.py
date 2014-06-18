# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_auto_20140618_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='total',
        ),
    ]
