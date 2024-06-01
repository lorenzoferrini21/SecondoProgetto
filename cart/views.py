from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from store.models import Store


# Create your views here.

@login_required
def add_to_cart(request, store_id):
    product = get_object_or_404(Store, id=store_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.quantity = 1
    cart_item.save()

    return redirect('store:store')


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart/cart.html', {'cart_items': cart_items})


@login_required
def remove_from_cart(request, store_id):
    cart_item = get_object_or_404(CartItem, id=store_id)
    cart_item.delete()
    return redirect('cart:view_cart')
