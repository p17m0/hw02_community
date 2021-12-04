from . import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='posts'),
    # Страница со списком мороженого
    path('posts_list/', views.posts_list, name='posts_list'),
    path('group/<slug:slug>/', views.group_posts),
]
