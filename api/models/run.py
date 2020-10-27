from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.
class Run(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  date = models.CharField(max_length=100, default="date")
  # DateField(_("Date"), default=datetime.date.today)
  time = models.CharField(max_length=100, default="time")
  # TimeField
  distance = models.FloatField(null=True, blank=True, default=None)
  location = models.CharField(max_length=100, default="here")
  rpe = models.IntegerField(
      default=1,
      validators=[MaxValueValidator(100),
      MinValueValidator(1)]
  )
  notes = models.CharField(max_length=250, default="notes")
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The run on {self.date} of {self.distance} at {self.location} was rated as {self.rpe} out of 10 and took {self.time}."

  def as_dict(self):
    """Returns dictionary version of Run models"""
    return {
        'id': self.id,
        'date': self.date,
        'time': self.time,
        'distance': self.distance,
        'location': self.location,
        'rpe': self.rpe,
        'notes': self.notes,
        'owner': self.owner
    }
