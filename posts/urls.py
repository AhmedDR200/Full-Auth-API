# posts/urls.py
from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    LikeCreateView, LikeDeleteView
)

urlpatterns = [
    # posts/urls.py
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # comments/urls.py
    path('posts/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', CommentUpdateView.as_view(), name='comment-detail'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-update'),
    # likes/urls.py
    path('posts/<int:pk>/like/', LikeCreateView.as_view(), name='like-create'),
    path('likes/<int:pk>/', LikeDeleteView.as_view(), name='like-delete'),
]
