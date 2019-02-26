# Generated by Django 2.1 on 2019-02-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticket_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='image',
        ),
        migrations.AddField(
            model_name='ticket',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]