from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model
        fields = ['id', 'username', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model
        fields = ['username', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)

        )
        return user
    
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']

