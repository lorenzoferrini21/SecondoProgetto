from django.shortcuts import render
from .models import Store


# Create your views here.
def store(request):
    stores = Store.objects.all()
    return render(request, 'store/store.html', {'stores': stores})