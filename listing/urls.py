from .views import ListingListView, ListingDetailView, ListingDeleteView, ListingUpdateView, ListingCreateView
from django.urls import path

urlpatterns = [
    path('', ListingListView.as_view(), name='listing_list'),
    path('<uuid:pk>/', ListingDetailView.as_view(), name='listing_detail'),
    path('create/', ListingCreateView.as_view(), name='listing_create'),
    path('<uuid:pk>/update/', ListingUpdateView.as_view(), name='listing_update'),
    path('<uuid:pk>/delete/', ListingDeleteView.as_view(), name='listing_delete'),
]
