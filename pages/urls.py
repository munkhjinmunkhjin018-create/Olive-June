
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('bestseller/', views.bestseller, name='bestseller'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
]
