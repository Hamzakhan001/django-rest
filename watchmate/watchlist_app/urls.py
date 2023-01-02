
from django.urls import path,include
from watchlist_app.views import movieList


urlpatterns = [
    path('list/',movieList,name="movie-list")
]
