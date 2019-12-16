from django.urls import path, include
from .views import Home, signin, AuthorViewSet
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('autores', AuthorViewSet)

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('signin/', views.signin, name="signin"),
    path('api/', include(router.urls)),
]
