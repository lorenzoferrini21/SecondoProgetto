from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('users:register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already existing')
                return redirect('users:register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('users:login')
        else:
            messages.info(request, 'Passoword Not Matching')
            return redirect('users:register')
    return render(request, 'users/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('store:store')
        else:
            messages.info(request, 'Username or Password not matching')
            return redirect('users:login')
    return render(request, 'users/login.html')


def logout(request):
    auth.logout(request)
    return redirect('store:store')
