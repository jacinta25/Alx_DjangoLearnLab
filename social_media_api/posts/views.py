from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from . models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.exceptions import NotFound

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Like
from notifications.models import Notification

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

class UserFeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # Fetch users followed by the current user
        following_users = user.following.all()
        # Retrieve posts from these users, ordered by creation date
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        # Serialize the posts
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)

        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=404)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({'message': 'You have already liked this post'}, status=400)
        
        Notification.objects.create(
            recipient = post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )

        return Response({'message': 'Post like successfully'}, status=200)
    
class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)

        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=404)
            
        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({'error' : 'You have not liked this post'}, status=400)
            
        like.delete()
        return Response({'message': 'Post unliked successfully'}, status=200)
        