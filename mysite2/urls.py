from django.conf.urls import patterns, include, url
# from polls.views import HomeView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^polls/', include('polls.urls', namespace="polls")),
    (r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', HomeView.as_view(), name='home'),

)
