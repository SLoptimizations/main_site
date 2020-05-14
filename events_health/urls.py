from django.urls import path, re_path
from events_health import views

urlpatterns = [
    # path('guest/', views.guest_view, name='guest'),
    path('guest/', views.GuestView.as_view(), name='guest'),

]