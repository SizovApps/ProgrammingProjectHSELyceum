# Generated by Django 2.1 on 2019-02-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_remove_ticket_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, upload_to='ticket_image'),
        ),
    ]