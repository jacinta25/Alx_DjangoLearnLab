from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from . models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.exceptions import NotFound

from django_filters.rest_framework import DjangoFilterBackend

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@action(detail=True, methods=['post'])
def comment(self, request, pk=None):
    post = self.get_object()
    serializer = CommentSerializer(data=request.user)
    if serializer.is_valid():
        serializer.save(post=post, author=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

def perform_update(self, serializer):
    post = self.get_object()
    if post.author != self.request.user:
        raise NotFound("You cannot edit this post.")
    serializer.save()
def perform_destroy(self, instance):
    if instance.author != self.request.user:
        raise NotFound("You cannot delete this post.")
    instance.delete()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

