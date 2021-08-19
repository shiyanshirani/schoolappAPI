from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail, ReviewCreate

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='individual-movie'),

    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(),
         name='individual-stream'),

    path('stream/review/', ReviewList.as_view(), name='review-list'),


    path('stream/review/<int:pk>/', ReviewList.as_view(), name='review-list'),
    path('stream/<int:pk>/review/', ReviewDetail.as_view(), name='review-detail'),
    path('stream/<int:pk>/review-create/',
         ReviewCreate.as_view(), name='review-create')
# ]
