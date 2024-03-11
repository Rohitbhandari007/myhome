from django.contrib import admin
from django.urls import path, include
from .views import IndexView, HomeDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/<int:home_id>/', HomeDetailView.as_view(), name='home_detail'),
]
