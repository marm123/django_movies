from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    AGE_LIMIT_CHOICES = [
        (3, 3),
        (7, 7),
        (13, 13),
        (16, 16),
        (18, 18),
        (21, 21)
    ]
    age_limit = models.IntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(18), MinValueValidator(0)],
        choices=AGE_LIMIT_CHOICES
    )

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
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title} from {self.released}'
