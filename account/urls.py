from django.urls import path
from account.views import login_req
from account.views import register_req
from account.views import logout_req

urlpatterns = [
    path("login", login_req, name="login"),
    path("register", register_req, name="register"),
    path("logout", logout_req, name="logout"),
]
