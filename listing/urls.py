from django.urls import path
from .views import ListingListView, ListingDetailView, ListingCreateView, ListingUpdateView

urlpatterns = [
    path('', ListingListView.as_view(), name='listing_list'),
    path('<uuid:pk>', ListingDetailView.as_view(), name='listing_detail'),
    path('<uuid:pk>', ListingCreateView.as_view(), name='listing_create'),
    path('<uuid:pk>', ListingUpdateView.as_view(), name='listing_update'),
]
