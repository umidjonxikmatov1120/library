from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'pages', 'price', 'cover_image', 'isbn')


class BooksSerializers(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.IntegerField()
    pages = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    cover_image = serializers.URLField()
    isbn = serializers.CharField()


