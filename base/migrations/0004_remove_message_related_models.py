# Generated by Django 5.0.6 on 2024-05-31 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_message_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='related_models',
        ),
    ]
