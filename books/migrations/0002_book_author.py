# Generated by Django 3.2.9 on 2021-11-08 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.TextField(default='', verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
