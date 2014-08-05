from django.conf.urls import patterns, include, url
from django.contrib import admin

import User.urls
import User.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UserSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^User/TimerData/', User.views.TimerData, name="TimerData"),
    url(r'^User/ButtonNavigation/', User.views.ButtonNavigation, name="ButtonNavigation"),
    url(r'^User/ButtonOne/$', User.views.ButtonOne, name="ButtonOne"),
    url(r'^User/ButtonNavTimer/$', User.views.ButtonNavTimer, name="ButtonNavTimer"),
    # url(r'^AlmostThere', User.views.AlmostThere, name="AlmostThere"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^User/', include('User.urls')),
    url(r'^$', User.views.index, name='index'),
    # url(r'^.*$', include(User.urls)),
)
