# comments/urls.py
from django.urls import path
from .views import add_comment

urlpatterns = [
    path('add_comment/<int:news_id>/', add_comment, name='add_comment'),
]
