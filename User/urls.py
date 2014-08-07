from django.conf.urls import patterns, include, url

from User import views

urlpatterns = patterns(
		
    url(r'^/TimerData/$', views.TimerData, name="TimerData"),
    url(r'^/ButtonNavigation/$', views.ButtonNavigation, name="ButtonNavigation"),
    url(r'^/ButtonOne/$', views.ButtonOne, name="ButtonOne"),
    url(r'^/ButtonNavTimer/$', views.ButtonNavTimer, name="ButtonNavTimer"),
		url(r'^/ButtonOne/$', views.ButtonOne, name='ButtonOne'),
        url(r'^/AlmostThere/$',views.AlmostThere, name="AlmostThere"),
		url(r'^/$', views.index, name="index"),
		)
