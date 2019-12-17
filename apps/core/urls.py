from django.urls import path, include
from .views import Home, signin, AuthorViewSet
from django.urls import path
from .views import Home, signin, CategoryList, indicadores, pokemons
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('autores', AuthorViewSet)

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('categoria/',CategoryList.as_view(), name="category"),
    path('signin/', views.signin, name="signin"),
    path('api/', include(router.urls)),
    path('indicadores/', indicadores, name="indicadores"),
    path('pokemons/', pokemons, name="pokemons"),
    
]
