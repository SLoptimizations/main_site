from django.contrib import admin
from marketing.models import Subscriber, Campaign, Email

# Register your models here.
admin.site.register(Subscriber)
admin.site.register(Campaign)
admin.site.register(Email)