from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import SignUpView, CustomLoginView
urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/',SignUpView.as_view(),name='signup'),
path('register/', views.login_register_view, name='register'),
path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]