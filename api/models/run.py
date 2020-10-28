from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.
class Run(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  date = models.DateField(null=True)
  # in total seconds
  time = models.IntegerField(
        default=0,
        validators=[
          MinValueValidator(0)]
  )
  # TimeField
  average_spd = models.FloatField(
        default = 0,
        validators = [
          MinValueValidator(0)
        ]
  )
  average_pace = models.CharField(max_length=100, default="not calculated")
  distance = models.FloatField(null=True, blank=True, default=None)
  location = models.CharField(max_length=100, default="no location provided")
  rpe = models.IntegerField(
      default=1,
      validators=[MaxValueValidator(10),
      MinValueValidator(1)]
  )
  notes = models.CharField(max_length=250, default="no notes")
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
        'average_spd': self.average_spd,
        'average_pace': self.average_pace,
        'location': self.location,
        'rpe': self.rpe,
        'notes': self.notes,
        'owner': self.owner
    }

  def run_pace(self):
    miles_uncorrected = (self.time/60)/self.distance
    miles_in_minutes = floor(miles_uncorrected)
    remainder = miles_uncorrected - miles_in_minutes
    seconds = remainder * 60
    rounded_seconds = round(seconds)
    return f'{milesInMinutes}:{seconds} min/mile'
