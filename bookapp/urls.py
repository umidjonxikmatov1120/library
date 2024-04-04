# from .views import BookListView, BookRetrieveView, BookDeleteView, BookUpdateView, BookCreateView, BookListCreateView, BookUpdateDeleteView
from rest_framework.routers import SimpleRouter

from .views import BookListView, BookDetailView, BookViewSet
from django.urls import path

router = SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls
