from django.conf.urls import patterns, include, url

from User import views

urlpatterns = patterns(
		url(r'^btnClick/$', views.btnClick, name='btnClick'),
        url(r'^AlmostThere/$',views.AlmostThere, name="AlmostThere"),
		url(r'^$', views.index, name="index"),
		)
