# Generated by Django 4.2.4 on 2023-08-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0002_reply_feedlike_bookmark"),
    ]

    operations = [
        migrations.AddField(
            model_name="feed",
            name="email",
            field=models.EmailField(
                blank=True, max_length=100, null=True, verbose_name="email"
            ),
        ),
    ]
