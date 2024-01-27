from django.urls import path
from .views import (
    createUser, getUsers, getUser,
    updateUser, deleteUser
)

urlpatterns = [
    path('users/', getUsers, name='users'),
    path('users/<int:pk>/', getUser, name='user'),
    path('users/create/', createUser, name='create-user'),
    path('users/<int:pk>/update/', updateUser, name='update-user'),
    path('users/<int:pk>/delete/', deleteUser, name='delete-user'),
]