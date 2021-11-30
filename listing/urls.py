from django.urls import path
from .views import ListingListView, ListingDetailView

urlpatterns = [
    path('', ListingListView.as_view(), name='listing_list'),
    path('<uuid:pk>', ListingDetailView.as_view(), name='listing_detail'),
]
