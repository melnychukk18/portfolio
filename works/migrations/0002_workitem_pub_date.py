# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workitem',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 27, 21, 34, 35, 941940, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
