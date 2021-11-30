import uuid
from django.db import models
from django.urls import reverse


class Listing(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(max_length=200)
    introduction = models.CharField(max_length=255)
    description = models.TextField()
    county = models.CharField(max_length=150)
    town = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    listing_cover = models.ImageField(upload_to='listing/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("listing_detail", args=[str(self.id)])
