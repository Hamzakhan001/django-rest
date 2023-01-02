from django.shortcuts import render
from watchlist_app.models import Movie

# Create your views here.(class or function based)

def movieList(request):
    movies= Movie.objects.all()
    print(movies.values())
    
