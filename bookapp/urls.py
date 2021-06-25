from django.urls import path
from django.urls.conf import include
from .views import BookList,BookHistory, BookHistoryList
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Book API')

urlpatterns = [

    path('booklist/', BookList.as_view()),
    path('bookorder/update/<int:pk>/',BookHistory.as_view()),
    path('bookorder/create_list/',BookHistoryList.as_view()),
    path('', schema_view),
    
   
]