# Generated by Django 5.0.6 on 2024-06-24 16:10

import shop_product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop_product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="image",
            field=models.ImageField(
                null=True, upload_to=shop_product.models.product_images_path
            ),
        ),
    ]