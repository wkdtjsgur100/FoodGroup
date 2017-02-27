from django.db import models
from django.conf import settings


class Meeting(models.Model):
    maker = models.TextField()
    name = models.TextField()
    place = models.TextField()
    start_time = models.DateTimeField()
    image_path = models.ImageField(upload_to='media/')

    distance_near_univ = models.TextField()
    price_range = models.TextField()


class Applier(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.TextField()
    phone_number = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE)
