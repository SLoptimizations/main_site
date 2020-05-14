import traceback
import yagmail
from marketing.funcs.resources import *
from django.core.mail import get_connection, EmailMultiAlternatives
from django.core.mail import send_mass_mail, send_mail
import pytracking
from pytracking.html import adapt_html

message1 = ('try1', 'message', "marketing/templates/email_page.html", 'SLop<SLoptimizations@gmail.com>',
            ['SLoptimizations@gmail.com'])
message2 = (
'try2', 'message', "marketing/templates/email_page.html", 'SLoptimizations@gmail.com', ['SLoptimizations@gmail.com'])
# send_mass_mail((message1, message2), fail_silently=False)

headers = {
    "Return-Receipt-To": 'SLoptimizations@gmail.com',
    "Disposition-Notification-To": 'SLoptimizations@gmail.com',
}


def read_html(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        return template_file.read()


def prepare_html(html_file_name, json, url_id):
    new_html = read_html(html_file_name)
    json = Myjson(json).get()
    if json:
        html_details = json['html']

        for key in html_details:
            new_html = new_html.replace('{' + key + '}', html_details[key])
        new_html = new_html.replace('{user_id}', url_id)
        return new_html.replace('\n', '')

    else:
        return new_html.replace('\n', '')


def send_mass_html_mail(datatuple, fail_silently=False, user=None, password=None,
                        connection=None):
    """
    Given a datatuple of (subject, text_content, html_content, from_email,
    recipient_list), sends each message to each recipient list. Returns the
    number of emails sent.

    If from_email is None, the DEFAULT_FROM_EMAIL setting is used.
    If auth_user and auth_password are set, they're used to log in.
    If auth_user is None, the EMAIL_HOST_USER setting is used.
    If auth_password is None, the EMAIL_HOST_PASSWORD setting is used.

    """
    connection = connection or get_connection(
        username=user, password=password, fail_silently=fail_silently)

    messages = []
    for subject, text, html, from_email, recipient in datatuple:
        message = EmailMultiAlternatives(subject, text, from_email, recipient, headers=headers)
        html_content = prepare_html(html, 'marketing/funcs/Sapir.json', '1')
        new_html_email_text = adapt_html(
            html_content, extra_metadata={"customer_id": 1},
            click_tracking=True, open_tracking=True)
        message.attach_alternative(new_html_email_text, 'text/html')
        messages.append(message)
    return connection.send_messages(messages)


# send_mass_html_mail((message1, message2))

#
#
# def send_mail(to, campaign_json, url_id):
#     try:
#         c_json = Myjson(campaign_json).get()
#
#         # initializing the server connection
#         yag = yagmail.SMTP(user=c_json['login']['User'], password=c_json['login']['Password'])
#
#         # getting values into HTML
#         fixed_html = prepare_html(c_json, url_id)
#
#         # sending the email
#         yag.send(to=to, subject=c_json['email_subject'], contents=fixed_html)
#         print("Email sent successfully")
#
#     except:
#         traceback.print_exc()
#         print("Error, email was not sent")


# send_mail(to='shovallevi.w@gmail.com',
#           subject='dd',
#           html_file='html/b.html',
#           client_json='Sapir.json')
