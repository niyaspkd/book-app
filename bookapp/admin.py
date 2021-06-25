from django.contrib import admin

# Register your models here.
from  .models import Book, BookHistory

admin.site.register(Book)

admin.site.register(BookHistory)