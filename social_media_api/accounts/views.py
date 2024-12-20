from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer, FollowSerializer
from rest_framework.decorators import api_view
from posts.models import Post
from posts.serializers import PostSerializer

# Create your views here.
User = get_user_model

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = get_user_model().objects.filter(username=username).first()


        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=400)
    
@api_view(['POST'])
def follow_user(request, user_id):
    try:
        user_to_follow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if user_to_follow == request.user:
        return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

    request.user.follow(user_to_follow)
    return Response({'message': f'You are now following {user_to_follow.username}.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    request.user.unfollow(user_to_unfollow)
    return Response({'message': f'You have unfollowed {user_to_unfollow.username}.'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_feed(request):
    posts = Post.objects.filter(author__in=request.user.following.all()).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
    