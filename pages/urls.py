from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.homePage, name='pages-home'),
    path("menu/", views.menuPage, name='pages-menu')
]
