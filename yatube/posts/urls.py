from . import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='posts'),
    path('group/<slug:address>/', views.group_posts, name='posts_list'),
]
