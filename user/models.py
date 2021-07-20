
from django.db import models


class User(models.Model):
    GENDER_CHOICES = [('F', 'female'), ('M', 'male')]
    first_name = models.CharField('first name', max_length=100, null=True)
    last_name = models.CharField('last name', max_length=130, null=True, blank=True)
    username = models.CharField('username', max_length=50, null=True)
    profile = models.TextField('description', max_length=150)
    gender = models.CharField('gender', max_length=1, choices=GENDER_CHOICES, default='F')
    phone_number = models.CharField('phone number', max_length=11, blank=True)
    biography = models.CharField('biography', max_length=100, null=True)
    country = models.CharField('country', max_length=20, null=True)
    website = models.URLField('website')
    email = models.EmailField('email')
    register_date = models.DateTimeField('register date', auto_now=True)
    update_date = models.DateTimeField('update date', auto_now_add=True)
    credit = models.IntegerField('credit', default=20)
    friends = models.ManyToManyField("User", blank=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.username} register on {self.register_date}'

    def delete(self):
        delete_obj = f'{self.first_name}{self.last_name} deleted on'
        self.delete()
        return delete_obj

    def update_credit(self, amount):
        self.credit += amount
        self.save()

    def get_friends(self):

        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    def get_books(self):
        return self.user.all()

    def get_books_no(self):
        return self.user.all().count()


class RelationShip(models.Model):
    STATUS_CHOICES = [('A', 'accepted'), ('R', 'requested')]
    sender = models.ForeignKey("User", on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey("User", on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='N')
    created = models.DateTimeField('register date', auto_now_add=True)
    updated = models.DateTimeField('update date', auto_now=True)

    def __str__(self):
        return f'{self.sender}, {self.receiver}'
