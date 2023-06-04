from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner'),
)

# Create your models here.
class Swag(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('swags_detail', kwargs={'pk': self.id})
  
class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  # Create a M:M relationship with Toy
  # toys is the Related Manager
  swags = models.ManyToManyField(Swag)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
  def __str__(self):
    return f'{self.name} ({self.id})'
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'dog_id': self.id})

class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  
  dog = models.ForeignKey(
    Dog,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
