from . import views

from django.urls import path

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.posts_group, name='posts_group'),
]
