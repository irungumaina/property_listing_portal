from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "introduction",
                  "description", "price", "county", "town", "listing_cover"]
