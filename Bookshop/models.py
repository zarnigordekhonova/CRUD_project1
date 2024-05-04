from django.db import models

# Create your models here.

class Genres(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Books(models.Model):
    genre = models.ForeignKey(to='Genres', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    cover_type = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='conf/', blank=True, null=True)


    def __str__(self):
        return f'{self.title} {self.genre}'


