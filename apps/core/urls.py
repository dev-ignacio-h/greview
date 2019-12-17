from django.urls import path, include
from .views import Home, signin, AuthorViewSet
from django.urls import path
from .views import Home, signin, CategoryList, AdventureList, StrategyList, WarList, RaceList, MMORPGList
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('autores', AuthorViewSet)

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('categoria/',CategoryList.as_view(), name="category"),
    path('aventura/',AdventureList.as_view(), name="aventura"),
    path('estrategia/',StrategyList.as_view(), name="estrategia"),
    path('accionbelica/',WarList.as_view(), name="accionbelica"),
    path('carreras',RaceList.as_view(), name="carreras"),
    path('mmorpg',MMORPGList.as_view(), name="mmorpg"),
    path('signin/', views.signin, name="signin"),
    path('api/', include(router.urls)),
]
