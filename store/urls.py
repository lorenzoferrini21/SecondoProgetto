from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.store, name='store'),
    path('store_by_artist/', views.store_by_artist, name='store_by_artist'),
    path('filtered_store/<str:artist>/', views.filtered_store, name='filtered_store'),
]