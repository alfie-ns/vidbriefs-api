# Generated by Django 5.0.6 on 2024-06-24 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("youtube", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinteraction",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="youtube.user"
            ),
        ),
        migrations.AlterField(
            model_name="userinteraction",
            name="video",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="youtube.video"
            ),
        ),
    ]
