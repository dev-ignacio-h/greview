from django.urls import path
from .views import Home, signin, CategoryList
from . import views

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('categoria/',CategoryList.as_view(), name="category"),
    path('signin/', views.signin, name="signin"),
]
