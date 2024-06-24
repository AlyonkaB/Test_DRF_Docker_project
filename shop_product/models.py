import pathlib
import uuid

from django.db import models
from django.utils.text import slugify


def product_images_path(instance: "Products", filename: str) -> pathlib.Path:
    filename = ((f"{slugify(instance.title)} "
                f"- {uuid.uuid4()}")
                + pathlib.Path(filename).suffix)
    return (pathlib.Path("upload/products/")
            / pathlib.Path(filename))


class Products(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, upload_to=product_images_path)
