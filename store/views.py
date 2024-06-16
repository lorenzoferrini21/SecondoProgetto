from django.shortcuts import render
from .models import Store
from cart.models import CartItem


# Create your views here.
def store(request):
    stores = Store.objects.all()
    artists = Store.objects.values_list('artista', flat=True).distinct()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        cart_count = cart_items.count()
    else:
        cart_items = []
        cart_count = 0

    return render(request, 'store/store.html', {'stores': stores, 'cart_items': cart_items, 'cart_count': cart_count, 'artists': artists})


def filtered_store(request, artist):
    stores = Store.objects.filter(artista=artist)
    artists = Store.objects.values_list('artista', flat=True).distinct()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart__user=request.user)
    else:
        cart_items = []
    return render(request, 'store/store.html', {'stores': stores, 'cart_items': cart_items, 'artists': artists})
