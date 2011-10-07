from django.conf.urls.defaults import *
from nowdata.dataexplorer.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    
    (r'^$', home_page),
    (r'^about/$', about_page),
    (r'^contact/$', contact_page),
    (r'^community_services/$', services_page),
    (r'^help/$', help_page),

    (r'^indicators/$', all_indicators),

    (r'^indicators/by_year/$', all_years),
    (r'^indicators/by_year/(?P<year>[-\d]+)$', view_year),

    (r'^indicators/(?P<slug>[-\w]+)$', view_indicator),
    (r'^indicators/(?P<indicator_slug>[-\w]+)/(?P<resource_slug>[-\w]+)$', view_resource_iframe),
    

    # administrative views
    
    (r'^nowdata_admin/indicators/recently_added/$', admin_indicators_recently_added),
    (r'^nowdata_admin/indicators/without_resources/$', admin_indicators_without_resources),
    (r'^nowdata_admin/indicators/by_status/(?P<status_code>[\d]{1})$', admin_indicators_by_status),

)
