from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import GuestForm, HealthDeclarationForm, UploadFileForm, EventForm
from django.views.generic import TemplateView, CreateView
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView
from .models import Event, Guest
from .tables import SimpleTable
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import GuestFilter
from events_health.funcs.main import load_phones_from_xl
MAIN_SITE = 'http://sl-op.com:5656/'


# MAIN_SITE = 'http://127.0.0.1:8000/'
# Create your views here.

def index(request):
    return render(request, 'wedding/guest_register.html')


#
#
class ClientView(View):
    guests = Guest.objects.all()
    def get(self, request, *args, **kwargs):
        event = Event.objects.get(pk=kwargs['pk'])
        guests_filter = GuestFilter(request.GET, queryset=self.guests)
        upload_form = UploadFileForm()
        guests = guests_filter.qs
        return render(request, 'wedding/client.html',
                      {
                          'event': event,
                          'guests': guests,
                          'guests_filter': guests_filter,
                          'upload_form': upload_form,

                      })


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


class EventUpdateView(UpdateView):
    template_name = 'wedding/client_update.html'
    model = Event
    form_class = EventForm
    extra_context = {
        "header": "עריכת פרטי אירוע:",
        "comment": "*התמונות יוצגו באתר, ניתן להוסיף עד 3 תמונות. במידה ולא יועלו תמונות כלל יוצגו תמונות האתר.",

    }

    template_name_suffix = '_update_form'


class GuestUpdateView(UpdateView):
    template_name = 'wedding/client_update.html'
    model = Guest
    form_class = GuestForm
    extra_context = {
        "header": "עריכת פרטי אורח:",
        "comment": "*לאחר שמירת השינויים לא ניתן לשחזר את המידע הקודם.",

    }

    template_name_suffix = '_update_form'


class GuestCreateView(CreateView):
    template_name = 'wedding/client_update.html'
    model = Guest
    form_class = GuestForm
    extra_context = {
        "header": "הוספת אורח חדש:",
        "comment": " ",

    }

class ClientRegisterView(CreateView):
    template_name = 'wedding/client_register.html'
    model = Event
    fields = "__all__"


class FileView(View):
    form = UploadFileForm()
    def get(self, request, *args, **kwargs):
        return render(request, 'wedding/client_update.html',
                      {

                          'form': self.form,

                      })

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        # f=request.FILES['file']
        if form.is_valid():
            load_phones_from_xl(request.FILES['file'])

            # with open('some/file/name.txt', 'wb+') as destination:
            #     for chunk in f.chunks():
            #         destination.write(chunk)
            # handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
