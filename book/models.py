from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField('name', max_length=30)


class Book(models.Model):
    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتابها'
    STATUS = [('F', 'free'), ('B', 'borrowed'), ('D', 'deprecated')]
    name = models.CharField('book_name', max_length=100, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_year = models.DateTimeField('year of publication')
    record_Date = models.DateTimeField('Time to record books', auto_now_add=True, null=True)
    update_time = models.DateTimeField('update_time', auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS)

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
