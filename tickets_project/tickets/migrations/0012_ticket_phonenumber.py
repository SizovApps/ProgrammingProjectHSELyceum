# Generated by Django 2.1 on 2019-02-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_remove_ticket_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='phoneNumber',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
    ]
