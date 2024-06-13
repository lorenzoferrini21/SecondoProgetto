from django.shortcuts import render
from .models import Store
from cart.models import CartItem


# Create your views here.
def store(request):
    stores = Store.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart__user=request.user)
    else:
        cart_items = []

    return render(request, 'store/store.html', {'stores': stores, 'cart_items': cart_items})


def store_by_artist(request):
    artists = Store.objects.values_list('artist', flat=True).distinct()
    return render(request, 'store/store_by_artist.html', {'artists': artists})


def filtered_store(request, artist):
    stores = Store.objects.filter(artista=artist)

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart__user=request.user)
    else:
        cart_items = []

    return render(request, 'store/store.html', {'stores': stores, 'cart_items': cart_items})
