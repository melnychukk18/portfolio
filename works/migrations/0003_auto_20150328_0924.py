# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_workitem_thumb_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='workimage',
            name='image_alt',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workitem',
            name='image',
            field=models.ManyToManyField(to='works.WorkImage', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workitem',
            name='included',
            field=models.CharField(max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workitem',
            name='role',
            field=models.CharField(max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workitem',
            name='text',
            field=models.TextField(max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workitem',
            name='url',
            field=models.CharField(max_length=300, blank=True),
            preserve_default=True,
        ),
    ]
