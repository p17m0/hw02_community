from django.shortcuts import render, get_object_or_404

from .models import Group, Post


def index(request):
    posts = Post.posts.all()[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def posts_group(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
