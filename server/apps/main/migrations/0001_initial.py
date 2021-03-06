# Generated by Django 2.2.14 on 2020-07-24 15:43

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    """Add HackernewsPost model."""

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='HackernewsPost',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Hackernews post',
                'verbose_name_plural': 'Hackernews posts',
                'unique_together': {('title', 'url')},
            },
        ),
    ]
