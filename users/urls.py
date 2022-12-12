from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
