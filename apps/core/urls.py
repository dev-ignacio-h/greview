from django.urls import path
from .views import Home, signin
from . import views

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('signin/', views.signin, name="signin"),
]
