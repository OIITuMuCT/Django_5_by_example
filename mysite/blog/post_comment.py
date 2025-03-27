from django.views.decorators.http import require_POST
from .forms import CommentForm
from django.shortcuts import get_object_or_404, render
from .models import Post

@require_POST
def post_comment(request, post_id):
    """Adding comments to the post"""
    ##* 1. По id поста извлекаем опубликованный пост,
    # * используя функцию сокращенного доступа get_object_or_404().
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    ##* 2. Определяется переменная comment с изначальным значением None.
    # * Указанная переменная будет использоваться
    # * для хранения комментарного объекта при его создании.
    comment = None
    ##* 3. Создается экземпляр формы, используя переданные на обработку POST-данные,
    # * и проводится их валидация методом is_valid(). Если форма невалидна,
    # * то шаблон прорисовывается с ошибками валидации.
    # A comment was posted
    form = CommentForm(data=request.POST)
    ##* 4. Если форма валидна, то создается новый объект Comment, вызывая
    # * метод save() формы, и назначается переменной new_comment,
    # * как показано ниже:
    if form.is_valid():
        ##* 5. Метод save() создает экземпляр модели, к которой форма привязана
        # * и сохраняет его в базе данных. Если вызывать его, используя commit=False,
        # * то экземпляр модели создается, но не сохраняется в базе данных. Такой
        # * подход позволяет видоизменять объект перед его окончательным сохранением.
        # Create a Comment object without saving it to the database
        comment = form.save(commit=False)
        ##* 6. Пост назначается заданному комментарию:
        # Assign the post to the comment
        comment.post = post
        ##* 7. Новый комментарий создается в базе данных путем вызова его метода
        # * save():
        # Save the comment to the database
        comment.save()
    ##* 8. Прорисованный шаблон blog/post/comment.html, передавая объекты
    # * post, form и comment в контексте шаблона.
    return render(request, 'blog/post/comment.html', {'post': post, 'form': form, 'comment': comment})


def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(
        request, 
        'blog/post/comment.html'
        {
            'post': post, 
            'form': form, 
            'comment': comment
        }
    )
    
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(
        request, 'blog/post/comment.html',
        {
            'post':post,
            'form': form,
            'comment': comment,
        }
    )

def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment= form.save(commit=False)
        comment.post = post
        comment.save()
    return render(
        request, "blog/post/comment.html",
        {
            'post': post,
            'form': form,
            'comment': comment
        }
    )

def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(
        request, 'blog/post/comment.html',
        {
            'post': post,
            'form': form,
            'comment': comment
        }
    )