# Generated by Django 4.2.4 on 2023-12-03 04:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bookMng", "0009_alter_rating_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rating",
            name="user",
        ),
        migrations.AddField(
            model_name="rating",
            name="user",
            field=models.ManyToManyField(default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
