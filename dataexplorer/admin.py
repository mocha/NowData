from django.contrib import admin
from nowdata.dataexplorer.models import *

# add one of these for each model:
# admin.site.register(ModelName)

admin.site.register(State)
admin.site.register(County)
admin.site.register(City)
admin.site.register(ResourceFormat)
admin.site.register(ResourceVariable)
admin.site.register(Resource)
admin.site.register(Domain)
admin.site.register(DomainGroup)
admin.site.register(Geo_Agg)
admin.site.register(Source)
admin.site.register(Indicator)
