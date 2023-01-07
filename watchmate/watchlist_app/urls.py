from django.urls import path,include
from watchlist_app.api.views import WatchListAV,WatchListDetailAV,StreamPlatformListAV,StreamPlatformDetailAV


urlpatterns = [
	path('list/',WatchListAV.as_view(),name="movie-list"),
    path('<int:pk>',WatchListDetailAV.as_view(),name='movie-detail'),
    
    path('stream/',StreamPlatformListAV.as_view(),name="stream-platofrmlist")
    
]

