# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'work/images/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=2000)),
                ('client', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=500)),
                ('included', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=300)),
                ('thumbnail', models.FileField(upload_to=b'work/thumbnails/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ManyToManyField(to='works.WorkImage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='workitem',
            name='type',
            field=models.ManyToManyField(to='works.WorkType'),
            preserve_default=True,
        ),
    ]
