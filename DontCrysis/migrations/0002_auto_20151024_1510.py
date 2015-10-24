# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DontCrysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crisis',
            name='personName',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='crisis',
            name='personPhone',
            field=models.CharField(max_length=8),
        ),
    ]
