from django.urls import path
from .views import *

urlpatterns = [
    path('type/', GenresView.as_view(), name='type'),
    path('tag/', TagsView.as_view(), name='tag'),
    path('publishers/', PublishersView.as_view(), name='publishers'),
    path('games/', GamesView.as_view(), name='games'),
    path('upcoming_games/', UpComingView.as_view(), name='upcoming_games'),
]
