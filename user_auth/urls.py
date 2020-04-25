from django.urls import path
from user_auth import views


urlpatterns = [

    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("forgot_password", views.forgot, name="forgot"),

]
