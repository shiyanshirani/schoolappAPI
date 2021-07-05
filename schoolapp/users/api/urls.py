from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.UserProfileViewSet.as_view())
]