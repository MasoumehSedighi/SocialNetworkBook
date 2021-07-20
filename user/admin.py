from django.contrib import admin

# Register your models here.

from .models import User, RelationShip

admin.site.register(User)
admin.site.register(RelationShip)
