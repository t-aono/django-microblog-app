# Generated by Django 2.0.2 on 2019-03-24 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190324_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(blank=True, default='', null=True, verbose_name='本文'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media/', verbose_name='画像'),
        ),
    ]
