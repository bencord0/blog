# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('slug', models.SlugField(max_length=128, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('md', models.TextField()),
            ],
        ),
    ]
