from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.editMenu, name='ownerpages-editMenu'),
    path("signout/", views.signOut, name='ownerpage-signout'),
    path("inventory/", views.inventoryPage, name='ownerpage-inventory')
]
