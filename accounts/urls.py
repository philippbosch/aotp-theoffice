from django.conf.urls.defaults import *
from views import login

urlpatterns = patterns('',
	url(r'^login/$', 'django.contrib.auth.views.login', { 'template_name': 'accounts/login.html' }, name="accounts_login"),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name="accounts_logout"),
)
