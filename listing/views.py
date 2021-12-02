from django.shortcuts import render
from django.urls import reverse_lazy
# from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Listing


class ListingListView(ListView):
    model = Listing
    context_object_name = 'listing_list'
    template_name = 'listings/listing_list.html'


class ListingDetailView(DetailView):
    model = Listing
    context_object_name = 'listing'
    template_name = 'listings/listing_detail.html'


class ListingCreateView(CreateView):
    model = Listing
    success_url = reverse_lazy('listing_detail')
    context_object_name = 'listing_create'
    template_name = 'listings/listing_create.html'


class ListingUpdateView(UpdateView):
    model = Listing
    success_url = reverse_lazy('listing_detail')
    context_object_name = 'listing_update'
    template_name = 'listings/listing_update.html'
