import os.path
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_ROOT, 'media')}),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('accounts.urls')),
    (r'', include('attendance.urls')),
)
