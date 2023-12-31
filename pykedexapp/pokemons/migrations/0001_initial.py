# Generated by Django 4.1.7 on 2024-01-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pokemon",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("order", models.IntegerField()),
                ("name", models.CharField(max_length=30)),
                ("lvl", models.IntegerField()),
                ("xp", models.IntegerField()),
                ("number", models.IntegerField()),
                ("type_1", models.CharField(max_length=30)),
                ("type_2", models.CharField(max_length=30)),
                ("special_capacity", models.CharField(max_length=30)),
                ("memo", models.CharField(max_length=300)),
                ("atck", models.IntegerField(default=0)),
                ("defs", models.IntegerField(default=0)),
                ("atck_spe", models.IntegerField(default=0)),
                ("defs_spe", models.IntegerField(default=0)),
                ("speed", models.IntegerField(default=0)),
                ("hp", models.IntegerField()),
                ("team_id", models.IntegerField()),
                ("shiny", models.BooleanField(default=False)),
                ("image_url", models.CharField(max_length=100)),
                ("shiny_image_url", models.CharField(max_length=100)),
            ],
        ),
    ]
