# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DontCrysis', '0002_auto_20151024_1510'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
