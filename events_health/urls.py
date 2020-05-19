from django.urls import path, re_path
from events_health import views


app_name = 'events_health'

urlpatterns = [
    # path('guest/', views.guest_view, name='guest'),
    path('guest/', views.GuestView.as_view(), name='guest'),
    path('client/<str:pk>', views.ClientView.as_view(), name='client'),
    path('client/add-file/', views.FileView.as_view(), name='add-file'),

    path('client/update-event/<str:pk>', views.EventUpdateView.as_view(), name='update-event'),
    path('client/update-guest/<str:pk>', views.GuestUpdateView.as_view(), name='update-guest'),
    path('client/create-guest/<str:pk>', views.GuestCreateView.as_view(), name='create-guest'),
    path('client_register/', views.ClientRegisterView.as_view(), name='client_register'),
    # path('table/', views.TableView.as_view(), name='table'),
    # re_path(r'^update/(?P<pk>\d+)/$', views.EventUpdateView.as_view(), name='client')

]
