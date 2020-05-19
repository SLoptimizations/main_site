from django.db import models
from address.models import AddressField
from datetime import datetime
from django.urls import reverse
import uuid
from django.utils.text import slugify

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
    # url_id = models.UUIDField( default=str(uuid.uuid4()).split('-')[1], editable=False)
    url_id = models.CharField(max_length=7, default='', blank=True)

    def __str__(self):
        return self.url_id+","+self.partner1

    def get_absolute_url(self):
        return reverse("events_health:client", kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.headline)
        super(Event, self).save(*args, **kwargs)



class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, verbose_name='אירוע')
    name = models.CharField(max_length=60, blank=False, verbose_name='שם')
    age = models.PositiveIntegerField(verbose_name="גיל")
    address = AddressField(verbose_name="כתובת")
    phone = models.CharField(max_length=60, verbose_name="מספר טלפון")  # change to phone field
    # slug = models.SlugField(unique=True)


    def __str__(self):
        return self.name




