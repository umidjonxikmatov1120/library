from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BookSerializer
from .models import Book


# CRUD - Create, Retrieve(Read), Update, Delete
# class based views
# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookCreateView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookRetrieveView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDeleteView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookUpdateView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookListCreateView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"{len(books)} ta kitob mavjud",
            "books": serializer_data
        }

        return Response(data)

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {"status": "Ma'lumotlar bazasiga kitob qo'shildi",
                    "books": data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data

            data = {
                'status': "Successfully",
                "book": serializer_data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status': "False",
                'message': 'Kitob toplimadi'
            }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            book = get_object_or_404(Book.objects.all(), id=pk)
            data = request.data
            serializer = BookSerializer(instance=book, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                book_saved = serializer.save()
            return Response({
                'status': 'True', 'message': f"{book_saved} kitob yangilandi."
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status': 'False',
                'message': 'Kitob topilmadi'
            }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            book = get_object_or_404(Book, id=pk)
            book.delete()
            return Response({
                'status': 'Succesfully delete',
                'message': "Kitob o'chirilidi"
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status': 'False',
                'message': 'Kitob topilmadi'
            }, status=status.HTTP_404_NOT_FOUND)
