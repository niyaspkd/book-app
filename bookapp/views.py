from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book, BookHistory
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.views.generic.detail import DetailView

from .serializers import BookSerializer,BookHistorySerializer
# Create your views here.



class BookList(generics.ListAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#    permission_classes = [IsAdminUser]


class BookHistoryList(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated,)            
    queryset = BookHistory.objects.all()
    filter_fields = ('book__name', 'user__username',)
    serializer_class = BookHistorySerializer


    


class BookHistory(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = BookHistorySerializer
    queryset = BookHistory.objects.all()

