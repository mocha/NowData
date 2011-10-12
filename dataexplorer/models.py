from django.db import models
from autoslug.fields import AutoSlugField
from django.contrib.auth.models import User
import base64


class County(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    def __str__(self): return self.name




class ResourceFormat(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    def __str__(self): return self.name




class ResourceVariable(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    def __str__(self): return self.name
    class Meta: ordering = ["name"]




class Resource(models.Model):
    name = models.CharField(max_length=255, unique=True)
    indicator = models.ForeignKey("Indicator")
    resource_format = models.ForeignKey(ResourceFormat, null=True)
    url = models.URLField(blank=True, null=True)
    resource_file = models.FileField(upload_to="somewhere/", blank=True)
    variables = models.ManyToManyField(ResourceVariable, blank=True)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    notes = models.TextField(blank=True, null=True)
    admin_only_notes = models.TextField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    added_by = models.ForeignKey(User, related_name = "resources_added", blank=True, null=True)
    modified_on = models.DateTimeField(auto_now = True, blank=True, null=True)
    modified_by = models.ForeignKey(User, related_name = "resources_modified", blank=True, null=True)
    def __str__(self): return self.name
    def __unicode__(self): return u'%s' % (self.name)
    class Meta: ordering = ["name"]

    IndicatorResourceID = models.TextField(blank=True, null=True)
    ResourceTypeID = models.TextField(blank=True, null=True)
    ResourceLocationID = models.TextField(blank=True, null=True)
    OrignalDataSetFileInfo = models.TextField(blank=True, null=True)
    OriginalDataSetNotes = models.TextField(blank=True, null=True)
    ApplicationName = models.TextField(blank=True, null=True)
    DocID = models.TextField(blank=True, null=True)
    tblName = models.TextField(blank=True, null=True)
    CellVar = models.TextField(blank=True, null=True)
    CellVarHeading = models.TextField(blank=True, null=True)
    ColVar = models.TextField(blank=True, null=True)
    ColHeading = models.TextField(blank=True, null=True)
    NumberCategories = models.TextField(blank=True, null=True)
    CatVar1 = models.TextField(blank=True, null=True)
    CatVar1Heading = models.TextField(blank=True, null=True)
    CatVar2 = models.TextField(blank=True, null=True)
    CatVar2Heading = models.TextField(blank=True, null=True)
    CatVar3 = models.TextField(blank=True, null=True)
    CatVar3Heading = models.TextField(blank=True, null=True)




class Domain(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    # relationship goes the other way around - groups belong to domains
    # group = models.ForeignKey("DomainGroup")
    slug = AutoSlugField(populate_from='name', unique_with='name')
    def __str__(self): return self.name
    class Meta: ordering = ["name"]




class DomainGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    domain = models.ForeignKey(Domain)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    def __str__(self): return self.name
    class Meta: ordering = ["name"]




class Geo_Agg(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True) 
    slug = AutoSlugField(populate_from='name', unique_with='name')
    def __str__(self): return self.name




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
    def __str__(self): return self.name



class FocusProject(models.Model):
  name = models.CharField(max_length=255, unique=True)
  short_description = models.TextField(blank=True)
  full_description = models.TextField(blank=True)
  slug = AutoSlugField(populate_from='name', unique_with='name')
  def __str__(self): return self.name
  def __unicode__(self): return u'%s' % (self.name)
  class Meta: ordering = ["name"]



class Indicator(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    source = models.ForeignKey(Source, blank=True, null=True)
    counties = models.ManyToManyField(County, blank = True)
    levels_of_aggregation = models.ManyToManyField(Geo_Agg, blank=True)
    # domain = models.ManyToManyField(Domain, blank = True)
    domaingroup = models.ManyToManyField(DomainGroup, blank=True)

    focusproject = models.ForeignKey(FocusProject, blank=True, null=True)

    STATUS_CHOICES = ( (0, 'Unknown'), (1, 'Started, Incomplete'), (2, 'In Progress'), (3, 'Completed'), )
    status = models.IntegerField(choices=STATUS_CHOICES)

    slug = AutoSlugField(populate_from='name', unique_with='name')
    notes = models.TextField(blank=True, null=True)
    admin_only_notes = models.TextField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    added_by = models.ForeignKey(User, related_name = "indicators_added", blank=True, null=True)
    modified_on = models.DateTimeField(auto_now = True, blank=True, null=True)
    modified_by = models.ForeignKey(User, related_name = "", blank=True, null=True)

    def __str__(self): return self.name
    def __unicode__(self): return u'%s' % (self.name)
    class Meta: ordering = ["name"]
    
    CategorizedBy = models.TextField(blank=True, null=True)
    Date_Acq = models.TextField(blank=True, null=True)
    RenewalDate = models.TextField(blank=True, null=True)
    MOU = models.TextField(blank=True, null=True)
    SourceAgencyID = models.TextField(blank=True, null=True)
    OriginalSourceAgencyID = models.TextField(blank=True, null=True)
    FolderPath = models.TextField(blank=True, null=True)
    PrimaryContactID = models.TextField(blank=True, null=True)
    Secondary1ContactID = models.TextField(blank=True, null=True)
    Secondary2ContactID = models.TextField(blank=True, null=True)
    DataSource_url = models.TextField(blank=True, null=True)
    Intermediary_Contact = models.TextField(blank=True, null=True)
    DataPeriod = models.TextField(blank=True, null=True)
    Time_Unit = models.TextField(blank=True, null=True)
    Suggest_Denom = models.TextField(blank=True, null=True)
    Limitations = models.TextField(blank=True, null=True)
    Strengths = models.TextField(blank=True, null=True)
    Restraints = models.TextField(blank=True, null=True)
    Files = models.TextField(blank=True, null=True)
    Spec_Proj = models.TextField(blank=True, null=True)





class IndicatorGroup(models.Model):
  DomainID = models.IntegerField()
  IndicatorGroupID = models.IntegerField()
  IndicatorID = models.IntegerField()




class ResourceFile(models.Model):

  _data = models.TextField(db_column='data', blank=True)
  def set_data(self, data): self._data = base64.encodestring(data)
  def get_data(self): return base64.decodestring(self._data)
  data = property(get_data, set_data)

  IndicatorResourceID = models.TextField(blank=True, null=True)
  ProtectionCode = models.TextField(blank=True, null=True)
  AppType = models.TextField(blank=True, null=True)
  DocType = models.TextField(blank=True, null=True)
  DocSize = models.TextField(blank=True, null=True)
  DocDescription = models.TextField(blank=True, null=True)
  # Doc = models.TextField(blank=True, null=True)
  UploadUser = models.TextField(blank=True, null=True)
  DateUpdated = models.TextField(blank=True, null=True)
  IPAddress = models.TextField(blank=True, null=True)


