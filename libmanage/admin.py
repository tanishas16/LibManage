from django.contrib import admin
from .models import User, Book, Borrower
# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Borrower)


