from django.contrib import admin

# Register your models here.


from .models import Book, Author, Comment,Like

admin.site.register(Book)

admin.site.register(Comment)

admin.site.register(Like)