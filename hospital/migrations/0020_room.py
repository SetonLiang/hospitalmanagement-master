# Generated by Django 4.1.12 on 2023-11-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0019_nurse"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("room_num", models.CharField(max_length=10, null=True)),
                ("Total_beds", models.CharField(max_length=10, null=True)),
                ("Available_beds", models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
