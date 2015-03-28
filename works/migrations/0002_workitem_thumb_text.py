# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workitem',
            name='thumb_text',
            field=models.TextField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
