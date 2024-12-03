from django.urls import path
from .views import JokeListView

urlpatterns = [
    path('jokes/',JokeListView.as_view(),name='jokes-list')
]