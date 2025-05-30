from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import GroupSerializer, UserSerializer, PostSerializer, CommentSerializer

from blog.models import Post, Comment

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows users to be viewed or edited """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows groups to be viewed or edited """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    # permission_classes =[permissions.IsAuthenticated]
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer