from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from .models import Informacion
from .models import Informacion2
from .models import Informacion3
from .models import Informacion4



# Create your views here.

class HomePagueView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'listado'

class InformacionPagueView(ListView):
    model = Informacion
    template_name = 'informacion.html'
    context_object_name = 'listado'




    
    