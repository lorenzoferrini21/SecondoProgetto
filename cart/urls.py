from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:store_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.view_cart, name='view_cart'),
    path('remove/<int:store_id>/', views.remove_from_cart, name='remove_from_cart'),
]