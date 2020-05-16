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
    YES = 10
    NO = 5

    Q1 = dict(Q='האם את/ה סובל ממחלות רקע?', A=[
        (YES, 'לא'),
        (NO, 'כן'),

    ])
    Q2 = dict(Q='האם אתה בבידוד?', A=[
        (YES, 'לא'),
        (NO, 'כן'),

    ])
    q1 = forms.ChoiceField(choices=Q1['A'], label=Q1['Q'])
    q2 = forms.ChoiceField(choices=Q2['A'], label=Q2['Q'])
