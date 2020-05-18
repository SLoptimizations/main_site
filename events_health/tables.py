import django_tables2 as tables
from .models import Guest


class SimpleTable(tables.Table):
    class Meta:
        model = Guest
        template_name = "django_tables2/bootstrap.html"
        fields = ['name','phone']
