from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='individual-movie'),

    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream'),
]