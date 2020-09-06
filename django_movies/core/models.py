from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age_limit = models.IntegerField(null=True)

    def __str__(self):
        return self.name


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=120)
    rating = models.IntegerField(
        null=True, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    released = models.DateField(null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.title} from {self.released}'
