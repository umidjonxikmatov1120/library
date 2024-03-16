from .views import BookListView, book_list_view

from django.urls import path

urlpatterns = [
    path('', BookListView.as_view()),
    path('func/', book_list_view, name='book_list_view')
]
