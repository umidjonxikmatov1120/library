from .views import BookListView, BookRetrieveView, BookDeleteView, BookUpdateView, BookCreateView, BookListCreateView, BookUpdateDeleteView
from django.urls import path

urlpatterns = [
    path('', BookListView.as_view()),
    path('create/', BookCreateView.as_view()),
    path('<int:pk>/', BookRetrieveView.as_view()),
    path('<int:pk>/delete/', BookDeleteView.as_view()),
    path('<int:pk>/update/', BookUpdateView.as_view()),
    path('listcreate/', BookListCreateView.as_view()),
    path('<int:pk>/updatedelete/', BookUpdateDeleteView.as_view()),
]
