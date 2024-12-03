# Generated by Django 5.1.3 on 2024-12-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Jokes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=50)),
                ("joke", models.TextField(blank=True, null=True)),
                ("setup", models.TextField(blank=True, null=True)),
                ("delivery", models.TextField(blank=True, null=True)),
                ("nsfw", models.BooleanField(default=False)),
                ("political", models.BooleanField(default=False)),
                ("sexist", models.BooleanField(default=False)),
                ("safe", models.BooleanField(default=True)),
                ("lang", models.CharField(max_length=10)),
            ],
        ),
    ]
