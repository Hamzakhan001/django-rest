from django.urls import path,include
from watchlist_app.api.views import WatchListAV,WatchListDetailAV,StreamPlatformListAV,StreamPlatformDetailAV,ReviewList,ReviewDetail,ReviewCreate


urlpatterns = [
	path('list/',WatchListAV.as_view(),name="movie-list"),
    path('<int:pk>',WatchListDetailAV.as_view(),name='movie-detail'),
    
    path('stream/',StreamPlatformListAV.as_view(),name="stream-platofrmlist"),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name="stream-platofrmdetail"),
    
    # path('stream/<int:pk>/review',StreamPlatformDetailAV.as_view(),name="stream-platofrmdetail"),
    # path('stream/review/<int:pk>',ReviewDetail.as_view(),name='review-detail'),
    path('review',ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>/review-create',ReviewCreate.as_view(),name='review-create'),
    path('review/<int:pk>',ReviewDetail.as_view(),name='review-detail'),
    
]

