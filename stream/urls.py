from django.urls import path
from . import views

app_name = "stream"
urlpatterns = [
    path('', views.index, name="index"),
    path('interstellar', views.stream, name="stream"),
    path('movies', views.list_movies, name="movies")
]