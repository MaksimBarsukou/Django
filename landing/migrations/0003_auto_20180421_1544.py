# Generated by Django 2.0.4 on 2018-04-21 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20180420_1025'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Home_sub_titile',
            new_name='Home_subtitile',
        ),
        migrations.RenameField(
            model_name='home_subtitile',
            old_name='Home_sub_titile',
            new_name='Home_subtitile',
        ),
    ]