# Generated by Django 4.2.7 on 2024-05-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_anonymous_message_replied_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_alert',
            field=models.BooleanField(default=False),
        ),
    ]
