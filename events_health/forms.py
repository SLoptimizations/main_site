from django import forms
from .models import Guest
from django.utils.translation import gettext_lazy as _


class GuestForm(forms.ModelForm):
    # event = forms.For

    class Meta:
        model = Guest
        fields = ('name', 'age', 'address', 'phone')
        labels = {
            'name': _('שם מלא'),
            'age': _('גיל'),
            'address': _('כתובת'),
            'phone': _('טלפון'),
        }



class HealthDeclarationForm(forms.Form):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    Q1 = dict(Q='שאלה1', A=[
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ])
    q1 = forms.ChoiceField(choices=Q1['A'], label=Q1['Q'])
