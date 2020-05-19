
from .models import *
from django_filters import DateFilter, FilterSet, CharFilter
from django.utils.translation import gettext_lazy as _


class GuestFilter(FilterSet):

    name = CharFilter(field_name='name', lookup_expr='icontains', label='שם')
    address = CharFilter(field_name='address', lookup_expr='icontains', label='כתובת')
    class Meta:
        model = Guest
        fields = ['age', 'phone']
        exclude = ['event']

    # def __init__(self, *args, **kwargs):
    #     super(GuestFilter, self).__init__(*args, **kwargs)
    #     self.filters['manufacturer'].extra.update(
    #         {'empty_label': 'All Manufacturers'})

