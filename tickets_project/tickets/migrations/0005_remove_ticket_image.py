# Generated by Django 2.1 on 2019-02-22 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20190222_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='image',
        ),
    ]
