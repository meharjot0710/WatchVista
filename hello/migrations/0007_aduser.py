# Generated by Django 5.0.3 on 2024-04-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hello", "0006_product_delete_cart"),
    ]

    operations = [
        migrations.CreateModel(
            name="adUser",
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
                ("username", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
    ]
