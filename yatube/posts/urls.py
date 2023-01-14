# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком постов
    path('posts/', views.posts_list),
    # Отдельная страница с информацией о постах
    path('groups/<slug:slug>/', views.group_posts),
] 