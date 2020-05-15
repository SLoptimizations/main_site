from django.shortcuts import render, redirect
from .forms import GuestForm, HealthDeclarationForm
from django.views.generic import TemplateView, CreateView
from django.views import View
from .models import Event,Guest


# Create your views here.

def index(request):
    return render(request, 'wedding/guest_register.html')


class GuestView(View):
    template_name = 'guest_register.html'
    guest_form = GuestForm()
    health_form = HealthDeclarationForm()

    def get(self, request, *args, **kwargs):
        event_id = request.GET.get('id', '')
        stage = request.GET.get('stage', '')
        event = Event.objects.all().filter(url_id=event_id)[0]

        if stage == '1':
            # self.guest_form.event = event
            return render(request, 'wedding/guest_register.html',
                          {'form': self.guest_form,
                           'event': event
                           })
        elif stage == '2':
            return render(request, 'wedding/guest_register.html',
                          {
                           'form': self.health_form,
                           'event': event
                           })


    def post(self, request, *args, **kwargs):

        event_id = request.GET.get('id', '')
        stage = request.GET.get('stage', '')
        if stage == '1':
            self.guest_form = GuestForm(request.POST)
            if self.guest_form.is_valid():
                event = Event.objects.all().filter(url_id=event_id)[0]
                guest = self.guest_form.save()
                guest.event = event
                guest.save()
                return redirect('http://127.0.0.1:8000/guest/?id=222&stage=2')

        elif stage == '2':
            self.health_form = HealthDeclarationForm(request.POST)
            if self.health_form.is_valid():
                return redirect('http://127.0.0.1:8000/guest/?id=222&stage=3')

            return index(request)
        else:
            print('error')
