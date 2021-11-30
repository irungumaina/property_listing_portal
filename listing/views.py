from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Listing


class ListingListView(ListView):
    model = Listing
    context_object_name = 'listing_list'
    template_name = 'listings/listing_list.html'


class ListingDetailView(DetailView):
    model = Listing
    context_object_name = 'listing'
    template_name = 'listings/listing_detail.html'
