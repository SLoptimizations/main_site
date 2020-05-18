from django.urls import path, re_path
from events_health import views


app_name = 'events_health'

urlpatterns = [
    # path('guest/', views.guest_view, name='guest'),
    path('guest/', views.GuestView.as_view(), name='guest'),
    path('client/<str:url_id>', views.ClientView.as_view(), name='client'),
    path('client_register/', views.ClientRegisterView.as_view(), name='client_register'),
    path('table/', views.TableView.as_view(), name='table'),
    re_path(r'^update/(?P<pk>\d+)/$', views.UpdateView.as_view(), name='client')

]