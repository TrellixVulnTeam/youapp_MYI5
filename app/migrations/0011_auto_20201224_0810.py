# Generated by Django 3.1.4 on 2020-12-24 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201224_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='channel_id',
            field=models.CharField(default='', max_length=24),
        ),
    ]