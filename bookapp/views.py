from django.shortcuts import render
from rest_framework import generics
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
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BookDetailView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response(status=204)


# Function based views
# @api_view(['GET'])
# def book_list(request):
#     books = Book.objects.all()
#     serializer_data = BookSerializer(books, many=True).data
#     data = {
#         "status": f"{len(books)} ta kitob mavjud",
#         "books": serializer_data
#     }
#
#     return Response(data)
