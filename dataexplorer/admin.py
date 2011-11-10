from django.contrib import admin
from nowdata.dataexplorer.models import *
from django.contrib.flatpages.models import FlatPage

# add one of these for each model:
# admin.site.register(ModelName)


class IndicatorAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'year_start', 'year_end', 'dataset', 'counties', 'levels_of_aggregation', 'domaingroup', 'focusproject', 'status', 'notes', 'admin_only_notes', 'hidden_from_public')
        }),
        # ('Admin Options', {
        #     'classes': ('collapse', 'extrapretty'),
        #     'fields': ('added_on', 'added_by', 'modified_on', 'modified_by')
        # }),
        ('Legacy Data', {
            'classes': ('collapse',),
            'fields': ('CategorizedBy', 'Date_Acq', 'RenewalDate', 'MOU', 'SourceAgencyID', 'OriginalSourceAgencyID', 'FolderPath', 'PrimaryContactID', 'Secondary1ContactID', 'Secondary2ContactID', 'DataSource_url', 'Intermediary_Contact', 'DataPeriod', 'Time_Unit', 'Suggest_Denom', 'Limitations', 'Strengths', 'Restraints', 'Files', 'Spec_Proj'
)
        }),
    )



class ResourceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'indicator', 'resource_format', 'url', 'resource_file', 'notes', 'admin_only_notes')
        }),
        ('Legacy Data', {
            'classes': ('collapse',),
            'fields': ('variables', 'IndicatorResourceID', 'ResourceTypeID', 'ResourceLocationID', 'OrignalDataSetFileInfo', 'OriginalDataSetNotes', 'ApplicationName', 'DocID', 'tblName', 'CellVar', 'CellVarHeading', 'ColVar', 'ColHeading', 'NumberCategories', 'CatVar1', 'CatVar1Heading', 'CatVar2', 'CatVar2Heading', 'CatVar3', 'CatVar3Heading',)
        }),
    )







admin.site.register(County)
admin.site.register(ResourceFormat)
admin.site.register(ResourceVariable)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Domain)
admin.site.register(DomainGroup)
admin.site.register(Geo_Agg)
admin.site.register(Source)
admin.site.register(Dataset)
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(FocusProject)
admin.site.register(Document)




