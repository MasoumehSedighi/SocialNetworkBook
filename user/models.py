from django.db import models


class User(models.Model):
    first_name = models.CharField('first name', max_length=100, null=True)
    last_name = models.CharField('last name', max_length=100, null=True, blank=True)
    username = models.CharField('username', max_length=10,null=False)
    profile = models.TextField('description',max_length=150)
    gender = models.Choices('gender')
    phone_number = models.CharField('phone number', max_length=11,blank=True)
    biography = models.CharField('biography', null=True)
    country = models.CharField('country', null=True)
    website = models.URLField('website')
    email = models.EmailField('email')
    register_date = models.DateTimeField('register date',auto_now_add=True)
    update_date = models.DateTimeField('update date')
