from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db import models

class Subject(models.Model):
    """ Предмет, к которому относится курс"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        """ Возвращает название предмета """
        return self.title

class Course(models.Model):
    """ Модель курса, которая содержит модули """
    owner = models.ForeignKey(
        User,
        related_name='course_created',
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject,
        related_name='courses',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        """ Возвращает название курса """
        return self.title

class Module(models.Model):
    """ Модель модуля для курса """
    course = models.ForeignKey(
        Course,
        related_name='modules',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        """ Возвращает название модуля """
        return self.title

class Content(models.Model):
    """
    Модель контент содержит обобщенное отношение, 
    чтобы ассоциировать с ним разные типы содержимого 
    """
    module = models.ForeignKey(
        Module,
        related_name='contents',
        on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={"model__in": ("text", "video", "image", "file")},
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')

class ItemBase(models.Model):
    """ Абстрактная  модель, предоставляет поля всем моделям Content  """
    owner = models.ForeignKey(
        User,
        related_name='%(class)s_related',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title

class Text(ItemBase):
    """ Для хранения текстового содержимого """
    content = models.TextField()

class File(ItemBase):
    """ Для хранения файлов """
    content = models.FileField(upload_to='files')

class Image(ItemBase):
    """ Для хранения изображений """
    content = models.ImageField(upload_to='images')

class Video(ItemBase):
    """ Для хранения видео """
    url = models.URLField()
