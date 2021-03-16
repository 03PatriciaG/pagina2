from django.urls import path
from .views import HomePagueView, InformacionPagueView

urlpatterns = [
    path('', HomePagueView.as_view(), name = 'home'),
    path('informacion', InformacionPagueView.as_view(), name = 'informacion'),
    
]