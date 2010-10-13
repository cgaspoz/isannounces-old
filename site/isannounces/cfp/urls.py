from django.conf.urls.defaults import *

urlpatterns = patterns('cfp.views',
    (r'^test', 'test'),
    (r'^$', 'index'),
#    (r'^(?P<poll_id>\d+)/$', 'detail'),
#    (r'^(?P<poll_id>\d+)/results/$', 'results'),
#    (r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)