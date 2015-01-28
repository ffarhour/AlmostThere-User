from django.conf.urls import patterns, include, url
from django.contrib import admin

import User.urls
import User.views

import homepage.urls
import homepage.views

import WebApp.urls
import WebApp.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UserSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^AlmostThere', User.views.AlmostThere, name="AlmostThere"),
    url(r'^admin', include(admin.site.urls)),
    url(r'^User', include('User.urls')),
    url(r'^WebApp', include("WebApp.urls")),
    url(r'homepage', include('homepage.urls')),
    url(r'^$', homepage.views.index, name='index'),
    # url(r'^.*$', include(User.urls)),
)
