from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:store_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.view_cart, name='view_cart'),
    path('remove/<int:store_id>/<str:redirect_to>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
path('checkout_single_item/<int:store_id>/', views.checkout_single_item, name='checkout_single_item'),
]