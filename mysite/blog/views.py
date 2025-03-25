from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    """ Выводит список постов на экран """
    posts = Post.published.all()
    return render(
        request, 'blog/post/list.html',
        {'posts': posts}
    )

def post_detail(request, id):
    """ Детали поста """
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    return render(request, 'blog/post/detail.html', {'post': post})