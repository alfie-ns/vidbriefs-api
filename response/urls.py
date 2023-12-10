from django.urls import path
from .views import GetYoutubeUrl



urlpatterns = [
    path('get_youtube_transcript/', GetYoutubeUrl.as_view(), name='get_youtube_transcript')
]