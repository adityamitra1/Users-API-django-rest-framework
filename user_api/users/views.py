from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import User
from django.db.models import Q
from .serializers  import UserSerializer

# Create your views here.

class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter,)
	search_fields = ('first_name','last_name')
	ordering_fields = ('username', 'email')
	filter_fields = ('first_name','last_name')
