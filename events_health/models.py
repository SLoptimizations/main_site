from django.db import models
from address.models import AddressField
from datetime import datetime



# Create your models here.

class Event(models.Model):
    partner1 = models.CharField(max_length=60, blank=False)
    partner2 = models.CharField(max_length=60, blank=False)
    event_location = AddressField()
    date = models.DateField(default='2020-06-14')
    hall_name = models.CharField(max_length=60, blank=False)
    img1 = models.URLField(default='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-1181856013.jpg')
    img2 = models.URLField(default='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-1181856013.jpg')
    img3 = models.URLField(default='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-1181856013.jpg')
    url_id = models.CharField(max_length=7, default='', blank=True)

    def __str__(self):
        return self.url_id


class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=60, blank=False)
    age = models.IntegerField(default=0)
    address = AddressField()
    phone = models.CharField(max_length=60)  # change to phone field

    def __str__(self):
        return self.name

