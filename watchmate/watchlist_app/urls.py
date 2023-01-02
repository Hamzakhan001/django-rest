
from django.urls import path,include
from watchlist_app.views import movieList,movie_detail


urlpatterns = [
    path('list/',movieList,name="movie-list"),
    path('<int:pk>',movie_detail,name="movie-detail")
]
