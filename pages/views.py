
from django.shortcuts import render

def home(request):
    return render(request, 'pages/index.html', {'active_page': 'home'})

def shop(request):
    return render(request, 'pages/shop.html', {'active_page': 'shop'})

def bestseller(request):
    return render(request, 'pages/bestseller.html', {'active_page': 'bestseller'})

def wishlist(request):
    return render(request, 'pages/wishlist.html', {'active_page': 'wishlist'})

def search(request):
    return render(request, 'pages/search.html', {'active_page': 'search'})

def profile(request):
    return render(request, 'pages/profile.html', {'active_page': 'profile'})
