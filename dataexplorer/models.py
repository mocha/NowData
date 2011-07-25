from django.db import models
from autoslug.fields import AutoSlugField
from easy_thumbnails.fields import *
from django.contrib.auth.models import User


class State(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    notes = models.TextField(blank=True)
    added_on = models.DateTimeField(auto_now_add = True)
    added_by = models.ForeignKey(User, related_name = "states_added")
    modified_on = models.DateTimeField(auto_now = True)
    modified_by = models.ForeignKey(User, related_name = "states_modified")
    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    state = models.ForeignKey(State)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    added_on = models.DateTimeField(auto_now_add = True)
    added_by = models.ForeignKey(User, related_name = "countys_added")
    modified_on = models.DateTimeField(auto_now = True)
    modified_by = models.ForeignKey(User, related_name = "countys_modified")
    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    state = models.ForeignKey(State)
    county = models.ForeignKey(County)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    added_on = models.DateTimeField(auto_now_add = True)
    added_by = models.ForeignKey(User, related_name = "cities_added")
    modified_on = models.DateTimeField(auto_now = True)
    modified_by = models.ForeignKey(User, related_name = "cities_modified")
    def __str__(self):
        return self.name


class ResourceFormat(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon = ThumbnailerImageField( 
        upload_to='images/resource_format/%Y/%m/%d',
        resize_source=dict(size=(64, 64)),
        null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    notes = models.TextField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    added_by = models.ForeignKey(User, related_name = "resourceformats_added", blank=True, null=True)
    modified_on = models.DateTimeField(auto_now = True, blank=True, null=True)
    modified_by = models.ForeignKey(User, related_name = "resourceformats_modified", blank=True, null=True)
    def __str__(self):
        return self.name


class ResourceVariable(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon = ThumbnailerImageField( 
        upload_to='images/resource_format/%Y/%m/%d',
        resize_source=dict(size=(64, 64)),
        null=True, blank=True)    
    slug = AutoSlugField(populate_from='name', unique_with='name')
    notes = models.TextField(blank=True)
    added_on = models.DateTimeField(auto_now_add = True)
    added_by = models.ForeignKey(User, related_name = "resourcevariables_added")
    modified_on = models.DateTimeField(auto_now = True)
    modified_by = models.ForeignKey(User, related_name = "resourcevariables_modified")
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]

class Resource(models.Model):
    name = models.CharField(max_length=255, unique=True)
    indicator = models.ForeignKey("Indicator")
    resource_format = models.ForeignKey(ResourceFormat, null=True)
    url = models.URLField(blank=True, null=True)
    resource_file = models.FileField(upload_to="somewhere/", blank=True)
    variables = models.ManyToManyField(ResourceVariable, blank=True)
    image = ThumbnailerImageField( 
        upload_to='images/resource/%Y/%m/%d',
        resize_source=dict(size=(300, 300)),
        null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    notes = models.TextField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    added_by = models.ForeignKey(User, related_name = "resources_added", blank=True, null=True)
    modified_on = models.DateTimeField(auto_now = True, blank=True, null=True)
    modified_by = models.ForeignKey(User, related_name = "resources_modified", blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
    def __unicode__(self):
        return u'%s' % (self.name)

    # data importing fields - these need to get organized in to other data models
    # meanwhile, they live here because that's where the old data had them
    #     
    # IndicatorResourceID = models.CharField(max_length=255, blank=True, null=True)
    # IndicatorID = models.CharField(max_length=255, blank=True, null=True)
    # ResourceTypeID = models.CharField(max_length=255, blank=True, null=True)
    # ResourceLocationID = models.CharField(max_length=255, blank=True, null=True)
    # OrignalDataSetFileInfo = models.CharField(max_length=255, blank=True, null=True)
    # OriginalDataSetNotes = models.CharField(max_length=255, blank=True, null=True)
    # ReportTitle = models.CharField(max_length=255, blank=True, null=True)
    # ApplicationName = models.CharField(max_length=255, blank=True, null=True)
    # DocID = models.CharField(max_length=255, blank=True, null=True)
    # tblName = models.CharField(max_length=255, blank=True, null=True)
    # CellVar = models.CharField(max_length=255, blank=True, null=True)
    # CellVarHeading = models.CharField(max_length=255, blank=True, null=True)
    # ColVar = models.CharField(max_length=255, blank=True, null=True)
    # ColHeading = models.CharField(max_length=255, blank=True, null=True)
    # NumberCategories = models.CharField(max_length=255, blank=True, null=True)
    # CatVar1 = models.CharField(max_length=255, blank=True, null=True)
    # CatVar1Heading = models.CharField(max_length=255, blank=True, null=True)
    # CatVar2 = models.CharField(max_length=255, blank=True, null=True)
    # CatVar2Heading = models.CharField(max_length=255, blank=True, null=True)
    # CatVar3 = models.CharField(max_length=255, blank=True, null=True)
    # CatVar3Heading = models.CharField(max_length=255, blank=True, null=True)
    # 
    


class Domain(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    icon = ThumbnailerImageField( 
        upload_to='images/domain/%Y/%m/%d',
        resize_source=dict(size=(64, 64)),
        null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    notes = models.TextField(blank=True)
    added_on = models.DateTimeField(auto_now_add = True)
    added_by = models.ForeignKey(User, related_name = "domains_added")
    modified_on = models.DateTimeField(auto_now = True)
    modified_by = models.ForeignKey(User, related_name = "domains_modified")
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]




class DomainGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    domain = models.ForeignKey(Domain)
    icon = ThumbnailerImageField( 
        upload_to='images/domain_group/%Y/%m/%d',
        resize_source=dict(size=(64, 64)),
        null=True, blank=True
    )
    slug = AutoSlugField(populate_from='name', unique_with='name')
    notes = models.TextField(blank=True)
    added_on = models.DateTimeField(auto_now_add = True)
    added_by = models.ForeignKey(User, related_name = "Domaingroups_added")
    modified_on = models.DateTimeField(auto_now = True)
    modified_by = models.ForeignKey(User, related_name = "Domaingroups_modified")
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]




class Geo_Agg(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True) 
    slug = AutoSlugField(populate_from='name', unique_with='name')
    notes = models.TextField(blank=True)
    added_on = models.DateTimeField(auto_now_add = True)
    added_by = models.ForeignKey(User, related_name = "indicatorlevelofagg_added")
    modified_on = models.DateTimeField(auto_now = True)
    modified_by = models.ForeignKey(User, related_name = "indicatorlevelofagg_modified")
    def __str__(self):
        return self.name




class Source(models.Model):
    name = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255, blank=True)
    display_url = models.URLField(blank=True)
    dataset_name = models.CharField(max_length=255, blank=True)
    contact_name = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    added_on = models.DateTimeField(auto_now_add = True)
    added_by = models.ForeignKey(User, related_name="sources_added")
    modified_on = models.DateTimeField(auto_now = True)
    modified_by = models.ForeignKey(User, related_name = "sources_modified")
    slug = AutoSlugField(populate_from='name', unique_with='name')
    def __str__(self):
        return self.name




class Indicator(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    source = models.ForeignKey(Source, blank=True, null=True)
    domain = models.ManyToManyField(Domain, blank = True)
    counties = models.ManyToManyField(County, blank = True)
    domaingroup = models.ManyToManyField(DomainGroup, blank=True)
    levels_of_aggregation = models.ManyToManyField(Geo_Agg, blank=True)
    image = ThumbnailerImageField( 
      upload_to='images/indicator/%Y/%m/%d',
      resize_source=dict(size=(300, 300)),
      null=True, blank=True)
    in_focus = models.BooleanField()
    slug = AutoSlugField(populate_from='name', unique_with='name')
    notes = models.TextField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    added_by = models.ForeignKey(User, related_name = "indicators_added", blank=True, null=True)
    modified_on = models.DateTimeField(auto_now = True, blank=True, null=True)
    modified_by = models.ForeignKey(User, related_name = "", blank=True, null=True)
    STATUS_CHOICES = (
      (0, 'Unknown'),
      (1, 'Started, Incomplete'),
      (2, 'In Progress'),
      (3, 'Completed'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
    def __unicode__(self):
        return u'%s' % (self.name)
    
    # data importing fields - these need to get organized in to other data models
    # meanwhile, they live here because that's where the old data had them
    
    # CategorizedBy = models.CharField(max_length=255, blank=True, null=True)
    # FolderPath = models.CharField(max_length=255, blank=True, null=True)
    # DataSource_url = models.URLField(blank=True, null=True)
    # 
    # PrimaryContactID = models.CharField(max_length=255, blank=True, null=True)
    # Secondary1ContactID = models.CharField(max_length=255, blank=True, null=True)
    # Secondary2ContactID = models.CharField(max_length=255, blank=True, null=True)
    # Intermediary_Contact = models.CharField(max_length=255, blank=True, null=True)
    # 
    # Time_Unit = models.CharField(max_length=255, blank=True, null=True)
    # Suggest_Denom = models.CharField(max_length=255, blank=True, null=True)
    # Limitations = models.CharField(max_length=255, blank=True, null=True)
    # Strengths = models.CharField(max_length=255, blank=True, null=True)
    # Restraints = models.CharField(max_length=255, blank=True, null=True)
    # Files = models.CharField(max_length=255, blank=True, null=True)
    # Spec_Proj = models.CharField(max_length=255, blank=True, null=True)
    # 
    # 






    
    




