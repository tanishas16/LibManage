from django.db import models


# Create your models here.
STATUS = (
    ('Available', 'Available'),
    ('Issued', 'Issued'),
)
class Book(models.Model):
    bname = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    yop = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default='Available')


class User(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)


class Borrower(models.Model):
    bu_id = models.IntegerField()
    b_id = models.IntegerField()
    b_name = models.CharField(max_length=150)
    due = models.DateField()
    fine = models.IntegerField(default=0)



