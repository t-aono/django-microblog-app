# Generated by Django 2.0.2 on 2019-03-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190323_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(default='', null=True, verbose_name='本文'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
    ]
