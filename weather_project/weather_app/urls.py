from django.urls import path
from . import views 

app_name = "weather_app"

urlpatterns = [
    path('', views.index, name="main"),
    path('weather_detail/<slug:ID>/', views.weather_detail, name="detail")
]