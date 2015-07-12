from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from .forms import LoginForm

# Create your views here.

def login(request):

    form = LoginForm()

    error_messages = []
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is None:
            error_messages.append('Username or Password are incorrect')
        else:
            if user.is_active:
                django_login(request, user)
                return redirect('posts:index')
            else:
                error_messages.append('The user is not active')
    context = {
        'errors': error_messages,
        'login_form': form,
    }
    return render(request, 'users/login.html', context)

def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('posts:index')