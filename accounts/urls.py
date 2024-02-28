from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from accounts.views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
]