from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from store.models import Store
from .decorators import login_or_register_required


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
    cart_items = CartItem.objects.filter(cart__user=request.user)
    return render(request, 'cart/cart.html', {'cart_items': cart_items})


@login_required
def remove_from_cart(request, store_id, redirect_to):
    cart_item = get_object_or_404(CartItem, id=store_id)
    cart_item.delete()
    if redirect_to == 'store':
        return redirect('store:store')
    else:
        return redirect('cart:view_cart')


@login_required
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
    except Cart.DoesNotExist:
        cart_items = []

    total_price = sum(item.product.prezzo * item.quantity for item in cart_items)

    if request.method == 'POST':
        cart_items.delete()
        return render(request, 'cart/checkout_success.html')

    return render(request, 'cart/checkout.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def checkout_single_item(request, store_id):
    product = get_object_or_404(Store, id=store_id)
    total_price = product.prezzo

    if request.method == 'POST':
        # Logica per completare l'acquisto del singolo prodotto
        # Potrebbe essere necessario aggiungere logica per tracciare l'acquisto nel database
        return render(request, 'cart/checkout_success.html')

    return render(request, 'cart/checkout_single.html', {'product': product, 'total_price': total_price})