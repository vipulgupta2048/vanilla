from django.urls import path
from .views import *

app_name = "user"

urlpatterns = [
    path('login/', LoginView, name="login"),
    path('logout/', LogoutView, name="logout"),
    path("", HomeView, name="user-home"),
]
