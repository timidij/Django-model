from django.db import models

from django.conf import settings


# Create your models here.
# class Title(models.Model):
#     name = models.CharField(max_length=200)

# class Text(models.Model):
#     name = models.TextField()

# class Author(models.Model):
#     name = models.ForeignKey(name, )

# class Created_date(models.Model):
#     name = models.DateTimeField()

# class Published_Date(models.Model):
#     name = models.DateTimeField()

class post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_Date = models.DateTimeField()
