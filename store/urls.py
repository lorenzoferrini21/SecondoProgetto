from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.store, name='store'),
    path('filtered_by_artist/<str:artist>/', views.filtered_store, name='filtered_store'),
]
