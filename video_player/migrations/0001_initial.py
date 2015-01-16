# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ultimo_login', models.DateTimeField()),
                ('conexoes', models.IntegerField()),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('url_hash', models.CharField(max_length=255)),
                ('url_expira_em', models.DateTimeField()),
                ('arquivo', models.CharField(max_length=255)),
                ('cliente', models.ForeignKey(to='video_player.Video')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
