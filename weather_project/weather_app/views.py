import requests
from django.shortcuts import render, get_object_or_404

from .forms import CityForm

from .models import City


def index (request):
    template="index.html"
    appid = "eb52d0ba3aac06c447312259fe57f4b8"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=" + appid
    
    if(request.method == "POST"):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()


    cities=City.objects.all()
    all_cities = []
    for city in cities:
        res =  requests.get(url.format(city.name)).json() 
        city_info = {
            "city" : city.name,
            "temp" : res["main"]["temp"],
            "icon" : res["weather"][0]["icon"],
            'ID' : city.id,
        }
        all_cities.append(city_info)

    context = {
        "all_info" : all_cities,
        "form" : form,
    }
    return render(request, template, context)


def weather_detail (request,ID):
    template="weather_detail.html"
    appid = "eb52d0ba3aac06c447312259fe57f4b8"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=" + appid
    
    if(request.method == "POST"):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    index = get_object_or_404(City, id=ID)
    cities=index.objects.all()
    for city in cities:
        res =  requests.get(url.format(city.name)).json() 
        city_info = {
            "city" : city.name,
            "temp" : res["main"]["temp"],
            "icon" : res["weather"][0]["icon"],
            'ID' : city.ID,
            "form" : form,
        }

    return render(request, template, city_info )