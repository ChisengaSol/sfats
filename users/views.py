from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import User, UserProfile
from .serializer import UserSerializer, UserProfileSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    search_fields = ['first_name', 'last_name']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer