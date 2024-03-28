from .models import Book
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'pages', 'price', 'cover_image', 'isbn')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # check author va title from database existence
        if Book.objects.filter(author=author, title=title).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitob sarlavhasi va muallifi bir xil bo'lgan kitobni yuklay olmaysiz"
                }
            )

        # kiritiladigan qiymat harflardan iboratmi yo'qmi tekshirib olish
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitobni sahifasi harflardan tashkil topgan bo'lishi kerak !"
                }
            )
        return data

    def validate_price(self, price):
        if 0 < price < 10_000_000_000:
            raise ValueError(
                {
                    'status': False,
                    'message': "Narx noto'g'ri kiritilgan"
                }
            )


# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     subtitle = serializers.CharField()
#     author = serializers.CharField()
#     image = serializers.URLField()
#     content = serializers.CharField()
#     isbn = serializers.CharField()
#     price = serializers.DecimalField(max_digits=20, decimal_places=2)
#
#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.subtitle = validated_data.get('subtitle', instance.subtitle)
#         instance.author = validated_data.get('author', instance.author)
#         instance.image = validated_data.get('image', instance.image)
#         instance.content = validated_data.get('content', instance.content)
#         instance.isbn = validated_data.get('isbn', instance.isbn)
#         instance.price = validated_data.get('price', instance.price)
#         instance.save()
#         return instance
