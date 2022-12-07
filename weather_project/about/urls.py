from django.urls import path
from . import views 

app_name = "about"

urlpatterns = [
    path('author/', views.author, name="author"),
    path('info/', views.info, name="info"),
]