from django.contrib import admin
from django.urls import path, re_path
from marketing import views
from pytracking.django import OpenTrackingView, ClickTrackingView
from django.conf.urls import url


urlpatterns = [
    # path('', views.AboutView.as_view(), name='about'),
    path('', views.register, name='about'),
    path('yoga_guide', views.VideoPageView.as_view(), name='all_video'),
    path('unsubscribe', views.UnsubscribeView.as_view(), name='unsubscribe'),

    url(r"^open/(?P<path>[\w=-]+)/$", views.MyOpenTrackingView.as_view(),
        name="open_tracking"),
    # re_path(
    #     "^click/(?P<path>[\w=-]+)/$", MyClickTrackingView.as_view(),
    #     name="click_tracking"),
]
