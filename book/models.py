from django.db import models
from user.models import User


# Create your models here.

class Author(models.Model):
    name = models.CharField('name', max_length=30)


class Book(models.Model):
    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتابها'
    STATUS = [('F', 'free'), ('B', 'borrowed'), ('D', 'deprecated')]
    name = models.CharField('book_name', max_length=100, null=True)
    publish_year = models.DateTimeField('year of publication')
    image = models.ImageField('books/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    liked = models.ManyToManyField("User", blank=True, related_name='likes')
    status = models.CharField(max_length=1, choices=STATUS)
    created = models.DateTimeField('Time to record books', auto_now_add=True, null=True)
    updated = models.DateTimeField('update_time', auto_now=True)



    @property
    def full_name(self):
        return f'{self.name},{self.author}'

    def __str__(self):
        return f'{self.name} and {self.update_time}'

    def change_status(self):
        if self.status == 'F':
            self.status = 'B'
        else:
            self.status = 'F'
        self.save()
        return self.status

    def get_publish_year(self):
        return self.publish_year.year





class Comment(models.Model):
    class Meta:
        ordering = ('-created',)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    LIKE_CHOICE = [('l', 'like'), ('d', 'dislike')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.CharField(max_length=3, choices=LIKE_CHOICE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def toggle(self):
        if self.like == 'l':
            self.like = 'd'
        else:
            self.like = 'l'
        self.save()


