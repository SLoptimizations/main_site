from django.shortcuts import render
from .forms import GuestForm, HealthDeclarationForm
from django.views.generic import TemplateView, CreateView
from django.views import View
from .models import Event


# Create your views here.

def index(request):
    return render(request, 'guest_register.html')


class GuestView(View):
    template_name = 'guest_register.html'
    guest_form = GuestForm()
    health_form = HealthDeclarationForm()

    def get(self, request, *args, **kwargs):
        event_id = request.GET.get('id', '')
        stage = request.GET.get('stage', '')
        event = Event.objects.all().filter(url_id=event_id)[0]

        if stage == '1':

            return render(request, 'guest_register.html',
                          {'form': self.guest_form,
                           'event': event
                           })
        elif stage == '2':
            return render(request, 'guest_register.html',
                          {
                           'form': self.health_form,
                           'event': event
                           })


    def post(self, request, *args, **kwargs):
        self.guest_form = GuestForm(request.POST)
        self.health_form = HealthDeclarationForm(request.POST)


        if self.guest_form.is_valid() and self.health_form.is_valid():
            event_id = request.GET.get('id', '')
            event = Event.objects.all().filter(url_id=event_id)[0]

            self.guest_form.save(commit=False)
            self.guest_form.event = event
            self.guest_form.save()

            self.health_form.save(commit=True)
            return index(request)
        else:
            print('error')
