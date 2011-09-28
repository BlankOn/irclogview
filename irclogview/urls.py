from django.conf.urls.defaults import patterns, url, include
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^admin/', include(admin.site.urls)),
    (r'^\+openid/', include('django_openid_auth.urls')),
)

urlpatterns += patterns('irclogview.views',
    url(r'^\+login/$', 'login', name='irclogview_login'),
    url(r'^\+logout/$', 'logout', name='irclogview_logout'),
    url(r'^(?P<name>[^/]+)/\+/$', 'bookmark_index', name='irclogview_bookmark_index'),
    url(r'^(?P<name>[^/]+)/\+/(?P<path>[a-zA-Z0-9_-]+)/$', 'bookmark_show', name='irclogview_bookmark_show'),
    url(r'^(?P<name>[^/]+)/(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})/$', 'show_log', name='irclogview_show'),
    url(r'^(?P<name>[^/]+)/$', 'channel_index', name='irclogview_channel'),
    url(r'^$', 'index', name='irclogview_index'),
)

