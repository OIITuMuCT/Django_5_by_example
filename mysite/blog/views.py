
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    """ Выводит список постов на экран """
    post_list = Post.published.all()
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    
    return render(
        request, 'blog/post/list.html',
        {'posts': posts}
    )

def post_detail(request, year, month, day, post):
    """ Детали поста """
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        
    )
    return render(request, 'blog/post/detail.html', {'post': post})