from django.shortcuts import render, get_object_or_404
from .models import Post, Group

POSTS_PER_PAGE = 10


def index(request):
    posts = Post.objects.all()[:POSTS_PER_PAGE]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts, 'title': title
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
