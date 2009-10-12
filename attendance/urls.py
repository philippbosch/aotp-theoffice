from django.conf.urls.defaults import *

urlpatterns = patterns('attendance.views',
    url(r'^$', 'dashboard', name="attendance_dashboard"),
    url(r'pay/$', 'pay', name="attendance_pay"),
)
