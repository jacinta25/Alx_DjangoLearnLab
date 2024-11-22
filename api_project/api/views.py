from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

from .permissions import IsAuthorOrReadOnly

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework import viewsets
# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
