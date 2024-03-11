from django.urls import re_path

from .consumers import HomeConsumer

websocket_urlpatterns = [
    re_path(r"ws/home/(?P<home_name>\w+)/$", HomeConsumer.as_asgi()),]
