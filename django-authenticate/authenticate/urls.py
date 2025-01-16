from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, CustomLogoutView
from . import views

app_name = "authenticate"
urlpatterns = [
    path("home/", views.IndexView, name='home'),
    path("register/", views.RegisterView, name='register'),
    path("login/", CustomLoginView.as_view(), name='login'),
    path("<str:username>/dashboard/", views.DashboardView, name='dashboard'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    #path('logout/', LogoutView.as_view(), name='logout'),
]