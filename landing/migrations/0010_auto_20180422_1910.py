# Generated by Django 2.0.4 on 2018-04-22 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0009_auto_20180422_1904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutsite',
            options={'verbose_name': 'О сайте', 'verbose_name_plural': 'О сайте'},
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Обратная связь', 'verbose_name_plural': 'Обратная связь'},
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Домашняя страница', 'verbose_name_plural': 'Домашняя страницы'},
        ),
    ]
