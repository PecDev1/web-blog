from django.urls import path,include
from comments.views import add_comment
from .views import (
    NewListView,
    NewUpdateView,
    NewDeleteView,
    NewDetailView,
NewCreateView,
CommentDeleteView
)

urlpatterns = [
    path('<int:pk>/edit/', NewUpdateView.as_view(), name='new_edit'),
    path('<int:pk>/', NewDetailView.as_view(), name='new_detail'),
    path('<int:pk>/delete/', NewDeleteView.as_view(), name='new_delete'),
    path('add_new/', NewCreateView.as_view(), name='add_new'),

    path('news/<int:news_id>/add_comment/', add_comment, name='add_comment'),
    path('news/', NewListView.as_view(), name='news'),
    path('<int:news_id>/', NewDetailView.as_view(), name='new_detail'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
    path('comments/', include('comments.urls')),  # Comments app URL'larini qo'shish
]
























