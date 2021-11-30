from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "county", "town", "price",
                    "introduction", "description",)


admin.site.register(Listing, ListingAdmin)
