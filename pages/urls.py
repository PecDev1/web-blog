from django.urls import path
from django.contrib.auth import views as auth_views

from .views import HomePageView, LogoutPageView, CallCenterPageView, AboutPaggeView, GamesPageView
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('call_center/', CallCenterPageView, name='call_center'),
    path('games/', GamesPageView, name='games'),
    path('about/', AboutPaggeView, name='about' ),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

