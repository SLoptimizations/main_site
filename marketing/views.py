from django.shortcuts import render
import uuid
from .models import Subscriber, Email, Campaign
from django.views.generic import TemplateView, View
from marketing.funcs.mail_management.main import send_mass_html_mail
from django.contrib.auth.models import User
from pytracking import Configuration
from pytracking.django import OpenTrackingView, ClickTrackingView
import datetime

# Create your views here.
def register(request):
    if request.method == "POST":

        # info = user_info_form.save(commit=False)
        data = request.POST
        user = Subscriber(
            username=data['username'],
            email=data['email'],
        )
        user.url_id = str(uuid.uuid4()).split('-')[1]
        campaign_id = request.POST.get('campaign_id', '')
        user.campaign_id = campaign_id
        emails = Email.objects.get(campaign_id=campaign_id, index=1)

        user.next_email_index = 1
        user.send_email_date = datetime.datetime.now()
        user.save()

        # send_mail(to=user.email,
        #           campaign_json='landing_page/funcs/Sapir.json',
        #           url_id=user.url_id)


    else:
        return render(request, 'landing_page/about.html')

    return render(request, 'landing_page/thanku_page.html')
#
#
# class VideoPageView(TemplateView):
#     template_name = 'video_page/video_page.html'
#
#     def get(self, request, *args, **kwargs):
#         url_id = request.GET.get('id', '')
#         try:
#             # user_id = int(request.POST['id'])
#             # user = UserInfo.objects.get(url_id=url_id)
#             user = Subscriber.objects.all().filter(url_id=url_id)[0]  # .get(url_id=url_id)
#             user.visits_counter = user.visits_counter + 1
#             user.save()
#
#         except User.DoesNotExist:
#             return render(request, 'landing_page/about.html')
#
#         return render(request, 'video_page/video_page.html')
#
#
# class UnsubscribeView(View):
#     template_name = 'email_page/unsubscribe.html'
#
#     def get(self, request, *args, **kwargs):
#         url_id = request.GET.get('id', '')
#         try:
#             # user_id = int(request.POST['id'])
#             user = Subscriber.objects.get(url_id=url_id)
#             user.unsubscribe = 1
#             user.save()
#
#         except User.DoesNotExist:
#             return render(request, 'landing_page/about.html')
#
#         return render(request, 'email_page/unsubscribe.html')
#
#     def post(self, request, *args, **kwargs):
#         url_id = request.GET.get('id', '')
#         try:
#             # url_id = int(request.POST['id'])
#             user = Subscriber.objects.all().filter(url_id=url_id)[0]  # .get(url_id=url_id)
#             user.unsubscribe = 0
#             user.save()
#
#         except User.DoesNotExist as e:
#             print(e)
#             return render(request, 'landing_page/about.html')
#         except:
#             return render(request, 'landing_page/about.html')
#
#         return render(request, 'email_page/unsubscribe.html')


class MyOpenTrackingView(OpenTrackingView):

    def notify_tracking_event(self, tracking_result):
        # Override this method to do something with the tracking result.
        # tracking_result.request_data["user_agent"] and
        # tracking_result.request_data["user_ip"] contains the user agent
        # and ip of the client.
        print(tracking_result)
        print(tracking_result.request_data["user_agent"])


        user_id = tracking_result.metadata["customer_id"]

        # user = Subscriber.objects.get(url_id=url_id)
        #             user.unsubscribe = 1
        #             user.save()




    # def notify_decoding_error(self, exception):
    #     # Called when the tracking link cannot be decoded
    #     # Override this to, for example, log the exception
    #     logger.log(exception)

    def get_configuration(self):
        # By defaut, fetchs the configuration parameters from the Django
        # settings. You can return your own Configuration object here if
        # you do not want to use Django settings.
        return Configuration()
