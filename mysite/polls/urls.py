from django.conf.urls import patterns, url

from polls import views #remove this and quote 'polls.views.index'

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
                       url(r'^(?P<poll_id>\d+)/results/$',views.results, name='results'),
                       url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
                       )
