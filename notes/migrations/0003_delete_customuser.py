# Generated by Django 4.1 on 2022-09-03 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
