from django.db import models
from address.models import AddressField
from datetime import datetime
from django.urls import reverse
import uuid
from django.utils.text import slugify

# Create your models here.

class Event(models.Model):
    partner1 = models.CharField(max_length=60, blank=False, verbose_name="פרטנר 1")
    partner2 = models.CharField(max_length=60, blank=False, verbose_name="פרטנר 2")
    event_location = AddressField(on_delete=models.CASCADE, verbose_name="כתובת מקום האירוע")
    date = models.DateField(default='2020-00-00', verbose_name="תאריך האירוע")
    hall_name = models.CharField(max_length=60, blank=False, verbose_name="שם האולם")
    img1 = models.URLField(default='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-1181856013.jpg', verbose_name='תמונה 1')
    img2 = models.URLField(default='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-1181856013.jpg', verbose_name='תמונה 2')
    img3 = models.URLField(default='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-1181856013.jpg', verbose_name='תמונה 3')
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
    NO = 0
    YES = 1
    STATUS = [
        (NO, 'לא רשום'),
        (YES, 'רשום')]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, verbose_name='אירוע')
    name = models.CharField(max_length=60, blank=False, verbose_name='שם')
    age = models.PositiveIntegerField(verbose_name="גיל")
    address = AddressField(on_delete=models.CASCADE, verbose_name="כתובת")
    phone = models.CharField(max_length=60, verbose_name="מספר טלפון")  # change to phone field
    status = models.CharField(max_length=60, choices=STATUS, default=NO, verbose_name="סטטוס")
    SMS_count = models.PositiveIntegerField(default=0, verbose_name="מספר הודעות שנשלחו")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("events_health:client", kwargs={'pk': self.pk})


