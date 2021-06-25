from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    book_count = models.IntegerField()


    def __str__(self):
        return self.name

class BookHistory(models.Model):
    rent_date = models.DateField(default=date.today ,blank=True, null=True)
    rent_time = models.TimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    return_date = models.DateField(blank=True, null=True)
    return_time = models.TimeField(blank=True, null=True) 


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=BookHistory)
def post_order(sender, instance, **kwargs):
        if (instance.return_date==None) & (instance.return_time==None):
            instance.book.book_count = instance.book.book_count - 1
        else:
            instance.book.book_count = instance.book.book_count + 1


    