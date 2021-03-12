from django.urls import path
from .views import HomePagueView

urlpatterns = [
    path('', HomePagueView.as_view(), name = 'home'),
]