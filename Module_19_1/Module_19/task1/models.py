from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=30, decimal_places=2)
    age = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(110)])


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=20, decimal_places=4)
    description = models.TextField(max_length=None)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

