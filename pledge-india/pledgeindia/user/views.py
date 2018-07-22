from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from .models import User
from .forms import LoginForm
# Create your views here.

def LoginView(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next') if request.GET.get('next', False) else settings.LOGIN_REDIRECT_URL)
            else:
                try:
                    user = User.objects.get(email=form.cleaned_data['email'])
                    if not user.is_active:
                        form.add_error(
                            None, "Your Login has been suspended. Contact Support for further info.")
                    else:
                        form.add_error(
                            None, "Username and Password doesn't match. Re-check the details. Password is case-sensitive.")
                except User.DoesNotExist as e:
                    form.add_error(
                        None, "No account exists with the given email.")
    else:
        form = LoginForm()
    
    return render(request, 'user/login.html', {'form': form})

def LogoutView(request):
    logout(request)

    return redirect(reverse("user:login"))
def HomeView(request):
    return render(request, 'user/home.html')
