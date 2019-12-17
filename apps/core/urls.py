from django.urls import path
from .views import Home, signin, indicadores, pokemons
from . import views

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('signin/', views.signin, name="signin"),
    path('indicadores/', indicadores, name="indicadores"),
    path('pokemons/', pokemons, name="pokemons"),
    
]
