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

  (r'^documents/$', all_documents),
  
  (r'^nowdata-admin/resources/unlinked/', admin_resources_unlinked),
  (r'^nowdata-admin/resources/no-indicator/', admin_resources_noindicator),

  (r'^nowdata-admin/indicators/no-description/', admin_indicators_nodescription),
  (r'^nowdata-admin/indicators/no-resources/', admin_indicators_noresources),
  (r'^nowdata-admin/indicators/by_status/(?P<status_code>[\d]{1})$', admin_indicators_by_status),

#  (r'^indicators/without_resources/$', admin_indicators_without_resources),

)
