from django.shortcuts import render, redirect
from .forms import GuestForm, HealthDeclarationForm
from django.views.generic import TemplateView, CreateView
from django.views import View
from .models import Event,Guest
import qrcode
from PIL import Image

MAIN_SITE = 'http://sl-op.com:5656/'
# MAIN_SITE = 'http://127.0.0.1:8000/'
# Create your views here.

def index(request):
    return render(request, 'wedding/guest_register.html')


class GuestView(View):
    template_name = 'wedding.html'
    guest_form = GuestForm()
    health_form = HealthDeclarationForm()

    def get(self, request, *args, **kwargs):
        event_id = request.GET.get('event_id', '')
        stage = request.GET.get('stage', '')
        event = Event.objects.all().filter(url_id=event_id)[0]

        if stage == '1':
            # self.guest_form.event = event
            return render(request, 'wedding/wedding.html',
                          {'form': self.guest_form,
                           'event': event
                           })
        elif stage == '2':
            return render(request, 'wedding/wedding.html',
                          {
                           'form': self.health_form,
                           'event': event
                           })
        elif stage == '3':
            # img = qrcode.make('Some data here')
            # img = img.get_image()
            # print(img)
            # print(img)
            result = request.GET.get('result', '')


    def post(self, request, *args, **kwargs):

        event_id = request.GET.get('event_id', '')
        stage = request.GET.get('stage', '')
        if stage == '1':
            self.guest_form = GuestForm(request.POST)
            if self.guest_form.is_valid():
                event = Event.objects.all().filter(url_id=event_id)[0]
                guest = self.guest_form.save()
                guest.event = event
                guest.save()

                return redirect(f'{MAIN_SITE}guest/?event_id={event_id}&stage=2&guest_id={guest.id}')

        elif stage == '2':
            self.health_form = HealthDeclarationForm(request.POST)
            guest_id = request.GET.get('guest_id', '')
            if self.health_form.is_valid():
                data = self.health_form.cleaned_data
                sum = 0
                # some calc func with result

                for label, a in data.items():
                    sum += int(a)
                result = 'green'

                # update DB with result here.


                # return by result

                # return redirect(f'http://127.0.0.1:8000/guest/?event_id=222&stage=3&guest_id={guest_id}')

                return render(request, 'wedding/result.html',
                              {
                                  'result': result,
                                  'guest_id': guest_id
                              })


        else:
            print('error')
