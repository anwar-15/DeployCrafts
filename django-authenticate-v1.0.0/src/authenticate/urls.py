from django.urls import path
from .views import CustomLoginView, CustomLogoutView
from . import views

app_name = "authenticate"
urlpatterns = [
    path("home/", views.IndexView, name='home'),
    path("register/", views.RegisterView, name='register'),
    path("login/", CustomLoginView.as_view(), name='login'),
    path("<str:username>/dashboard/", views.DashboardView, name='dashboard'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('verify_email/<str:token>/', views.verify_email, name='verify_email'),
    #path('logout/', LogoutView.as_view(), name='logout'),
]