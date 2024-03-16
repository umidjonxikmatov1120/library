from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # float: 9900.00

    cover_image = models.URLField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

