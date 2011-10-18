from django.conf.urls.defaults import *
from nowdata.dataexplorer.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  
  (r'^admin/', include(admin.site.urls)),
  
  (r'^indicators/$', all_indicators),
  (r'^indicators/(?P<slug>[-\w]+)$', view_indicator),
  (r'^indicators/(?P<indicator_slug>[-\w]+)/(?P<resource_slug>[-\w]+)$', view_resource_iframe),
  
  # administrative views
  
  (r'^indicators/recently_added/$', admin_indicators_recently_added),
  (r'^indicators/without_resources/$', admin_indicators_without_resources),
  (r'^indicators/by_status/(?P<status_code>[\d]{1})$', admin_indicators_by_status),

)
