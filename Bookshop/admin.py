from django.contrib import admin
from .models import Genres, Books

# Register your models here.

admin.site.register(Genres)
admin.site.register(Books)