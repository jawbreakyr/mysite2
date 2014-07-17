from django.conf.urls import patterns, url

from polls import views


urlpatterns = patterns('',
	url(r'^$', views.HomeView.as_view(), name='home'),
	url(r'^index/$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	# url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<poll_id>\d+)/votes/$', views.vote, name='vote'),
	url(r'^login/$', views.login, name='login'),
	url(r'^authen/$', views.authen_view, name='authen'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^loggedin/$', views.loggedin, name='loggedin'),
	url(r'^invalid/$', views.invalid_login, name='invalid'),

)