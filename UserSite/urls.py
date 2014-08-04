from django.conf.urls import patterns, include, url
from django.contrib import admin

import User.urls
import User.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UserSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^AlmostThere', User.views.AlmostThere, name="AlmostThere"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', include(User.urls)),
)
