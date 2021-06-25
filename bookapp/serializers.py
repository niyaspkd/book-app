from rest_framework import serializers
from .models import Book, BookHistory

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookHistorySerializer(serializers.ModelSerializer):
    book_name = serializers.ReadOnlyField(source='book.name')
    user_name = serializers.ReadOnlyField(source='user.username')

    
    class Meta:
        model = BookHistory
        read_only_fields = ('user_name', 'book_name')
        fields = '__all__'