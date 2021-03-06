from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from model_utils import Choices

AGE_LIMIT_CHOICES = Choices(
    (0, 'kids', 'kids'),
    (1, 'teens', 'teens'),
    (2, 'adults', 'adults')
)


class Country(models.Model):
    country = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('country',)

    def __str__(self):
        return self.country


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)

    age_limit = models.IntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(18), MinValueValidator(0)],
        choices=AGE_LIMIT_CHOICES
    )

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    class Meta:
        unique_together = ('name', 'surname')

    def __str__(self):
        return f'{self.name} {self.surname}'


class Movie(models.Model):
    title = models.CharField(max_length=120)
    rating = models.IntegerField(
        null=True, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    released = models.DateField(null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)
    countries = models.ManyToManyField(Country, related_name='movies')

    class Meta:
        unique_together = ('title', 'released', 'director')
        ordering = ['released']

    def __str__(self):
        return f'{self.title} from {self.released}'
