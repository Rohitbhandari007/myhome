from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Home, Room, Light


class IndexView(View):
    def get(self, request):
        homes = Home.objects.all()
        context = {
            "homes": homes,
        }
        return render(request, "index.html", context)


class HomeDetailView(View):
    def get(self, request, home_id):
        home = get_object_or_404(Home, id=home_id)
        rooms = Room.objects.filter(home=home)
        all_lights = Light.objects.filter(room__in=rooms)
        context = {
            "home": home,
            "rooms": rooms,
            "room_count": rooms.count(),
            "all_lights": all_lights,
        }
        return render(request, "home/home_detail.html", context)
