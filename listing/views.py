from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Listing
from .forms import ListingForm


class ListingListView(ListView):
    model = Listing
    paginate_by = 10
    context_object_name = 'listing_list'
    template_name = 'listings/listing_list.html'

    def get_queryset(self):
        return Listing.objects.all()


class ListingDetailView(DetailView):
    model = Listing
    context_object_name = 'listing'
    template_name = 'listings/listing_detail.html'


class ListingCreateView(CreateView):
    model = Listing
    message = ("The Listing has been created")
    form_class = ListingForm
    success_url = reverse_lazy('listing_list')
    context_object_name = 'listing_create'
    template_name = 'listings/listing_create.html'


class ListingUpdateView(UpdateView):
    model = Listing
    form_class = ListingForm
    success_url = reverse_lazy('listing_list')
    message = ("The Listing has been updated")
    context_object_name = 'listing_update'
    template_name = 'listings/listing_update.html'

    def get_queryset(self):
        return Listing.objects.all()


class ListingDeleteView(DeleteView):
    form_class = ListingForm
    success_url = reverse_lazy('listing_list')
    context_object_name = 'listing_delete'
    template_name = 'listings/listing_delete.html'

    def get_queryset(self):
        return Listing.objects.all()
