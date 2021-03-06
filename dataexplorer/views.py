from django.shortcuts import render_to_response
from django.template import RequestContext
from nowdata.dataexplorer.models import *
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required


import operator
def all_indicators(request):
  
  selected_formats = []
  selected_counties = []
  selected_geos = []
  title = ""
  subtitle = ""
  selected_domain = ""
  search_query = ""
  selected_domaingroup = ""
  selected_focusproject = ""
  advanced_options = False
  
  
  if request.GET:
    
    try:
      search_query = request.GET['search_query']
      if search_query != "":
        search_filter = Q(name__icontains = search_query) | Q(description__icontains = search_query) | Q(resource__name__icontains = search_query)
        title = "<em>Indicators matching:</em> \"" + search_query + "\""
      else:
        search_filter = Q()

    except:
      search_filter = Q()
      search_query = ""


    # set the domain
    try:
      selected_domain = request.GET['domain']
      domain_filter = Q(domaingroup__domain__slug = selected_domain)
      if not title:
        title = "<em>Exploring:</em> " + Domain.objects.get(slug = selected_domain).name
      else: 
        subtitle = subtitle + "Topics:" + Domain.objects.get(slug = selected_domain).name
    except: 
      domain_filter = Q()
      selected_domain = ""
      domaingroup_filter = Q()
      selected_domaingroup = ""
      
    
    # set the subdomain
    try:
      selected_domaingroup = request.GET['domaingroup']
      if selected_domaingroup:
        domaingroup_filter = Q(domaingroup__slug = selected_domaingroup)
        if selected_domaingroup: advanced_options = True
  
        if (not selected_domain) or (selected_domain == ""):
          domaingroup = DomainGroup.objects.get(slug = selected_domaingroup)
          selected_domain = Domain.objects.get(name = domaingroup.domain).slug
          # debug = selected_domain
        subtitle = subtitle + "Subtopic: " + DomainGroup.objects.get(slug = selected_domaingroup).name + "<br />"
      else:
        domaingroup_filter = Q()
        selected_domaingroup = ""
    except: 
      domaingroup_filter = Q()
      selected_domaingroup = ""


    try: 
      selected_counties = request.GET.getlist('selected_counties')
      if selected_counties:
        county_filter = reduce(operator.or_, [Q(counties__slug = str(county)) for county in selected_counties])      
        selected_county_subtitle_list = ""
        advanced_options = True
        for county in selected_counties:
          selected_county_subtitle_list = selected_county_subtitle_list + " " + County.objects.get(slug=county).name + ", "
        subtitle = subtitle + "Counties: " + selected_county_subtitle_list + "<br />"
      else:
        county_filter = Q()  
    except: county_filter = Q()


    try: 
      selected_geos = request.GET.getlist('selected_geos')
      geo_filter = reduce(operator.or_, [Q(levels_of_aggregation__slug = str(geo)) for geo in selected_geos])     
      selected_geo_subtitle_list = ""
      advanced_options = True
      for geo in selected_geos:
        selected_geo_subtitle_list = selected_geo_subtitle_list + " " + Geo_Agg.objects.get(slug=geo).name + ", "
      subtitle = subtitle + "Scopes: " + selected_geo_subtitle_list + "<br />"
    except: geo_filter = Q()


    try:
      selected_formats = request.GET.getlist('selected_formats')
      format_filter = reduce(operator.or_, [Q(resource__resource_format__slug = str(format)) for format in selected_formats])
      selected_format_subtitle_list = ""
      advanced_options = True
      for format in selected_formats:
        selected_format_subtitle_list = selected_format_subtitle_list + " " + format + ", "

      subtitle = subtitle + "Formats: " + selected_format_subtitle_list + "<br />"
    except: format_filter = Q()


    # set the focusproject
    try:
      selected_focusproject = request.GET['focusproject']
      focusproject_filter = Q(focusproject__slug = selected_focusproject)
      subtitle = subtitle + "Project: " + FocusProject.objects.get(slug = selected_focusproject).name
      advanced_options = True
    except: 
      focusproject_filter = Q()
      selected_focusproject = ""

    
    
    indicators = Indicator.objects.filter(
      search_filter,
      domain_filter,
      domaingroup_filter,
      format_filter,
      county_filter,
      geo_filter,
      focusproject_filter,
    ).distinct().exclude(hidden_from_public = True).order_by('-id')

  else:
    indicators = Indicator.objects.exclude(hidden_from_public = True).order_by('-id')
    subtitle = "Listing all indicators in our database"
    domain = ""
    format = ""
    county = ""

  all_formats = ResourceFormat.objects.all()
  all_geos = Geo_Agg.objects.all()
  all_domains = Domain.objects.exclude(id=99)
  all_focusprojects = FocusProject.objects.all()

  if selected_domain:
    all_domaingroups = DomainGroup.objects.filter(domain__slug = selected_domain)
  else:
    all_domaingroups = []
    
  if not title: title = "<em>Exploring:</em> All Indicators"
  
  # add indicator resource metadata to indicator object
  for indicator in indicators:
    formats = ResourceFormat.objects.all()
    indicator.formats = []
    for format in formats:
      format.count = Resource.objects.filter(resource_format = format).filter(indicator = indicator).distinct().count()
      if format.count > 0:
        indicator.formats.append(format)
      

  return render_to_response (
      'dataexplorer/indicator_list.html',
      { 
        'indicators': indicators, 
        'title': title,
        'subtitle': subtitle,
        'advanced_options':advanced_options,
        'search_query':search_query,
        
        'all_formats':all_formats,
        'selected_formats':selected_formats,
        
        'all_geos':all_geos,
        'selected_geos':selected_geos,
        
        'all_domains':all_domains,
        'selected_domain':selected_domain,
        
        'all_domaingroups':all_domaingroups,
        'selected_domaingroup':selected_domaingroup,

        'selected_focusproject':selected_focusproject,
        'all_focusprojects':all_focusprojects,
        
        'selected_counties':selected_counties,
        # 'debug':debug,
      }, 
      context_instance=RequestContext(request)
  )



import random
def view_indicator(request, slug):
    indicator = Indicator.objects.get(slug = slug)
    indicator_domains = []
    for domaingroup in indicator.domaingroup.all(): indicator_domains.append(domaingroup.domain)
    indicator_domains = set(indicator_domains)

    try:
      related_domaingroup = random.choice(indicator.domaingroup.all())
    except:
      related_domaingroup = ""
    
    try:
      related_domaingroup_indicators = related_domaingroup.indicator_set.all()[:2]
    except:
      related_domaingroup_indicators = ""

    return render_to_response (
        'dataexplorer/view_indicator.html', 
        {
          'indicator': indicator,
          'title': indicator.name,
          'indicator_domains':indicator_domains,
          'related_domaingroup': related_domaingroup,
          'related_domaingroup_indicators' : related_domaingroup_indicators,
        }, 
        context_instance=RequestContext(request)
    )



def view_resource_iframe(request, indicator_slug, resource_slug):
    indicator = Indicator.objects.get(slug = indicator_slug)
    resource = Resource.objects.get(slug = resource_slug)
    
    return render_to_response(
        'dataexplorer/view_resource_iframe.html',
        { 
          'indicator': indicator, 
          'resource': resource
        },
        context_instance=RequestContext(request)
    )




@login_required
def all_documents(request):
  documents = Document.objects.all()
  
  return render_to_response (
    'global/all_documents.html',
    {
      'title':"All Documents",
      'subtitle':'Newest documents first',
      'documents':documents,
    },
    context_instance=RequestContext(request) 
  )








@login_required
def admin_indicators_by_status(request, status_code):
  indicators = Indicator.objects.filter(status = status_code).order_by("added_on")
  if status_code == "0": code_name = "Unknown"
  elif status_code == "1": code_name = "Incomplete"
  elif status_code == "2": code_name = "In Progress"
  elif status_code == "3": code_name = "Completed"
  else: code_name = "ERR"

  return render_to_response (
  'dataexplorer/admin_indicator_list.html',
      { 
        'indicators': indicators, 
        'title': "<em>Admin:</em> Indicators marked " + code_name, 
        'subtitle': "Oldest indicators are at the top"
      }, 
      context_instance=RequestContext(request)
  )


@login_required
def admin_indicators_nodescription(request):
  indicators = Indicator.objects.filter(description = "").order_by("added_on")
  return render_to_response (
  'dataexplorer/admin_indicator_list.html',
      { 
        'indicators': indicators, 
        'title': "<em>Admin:</em> Indicators without descriptions", 
        'subtitle': "Oldest indicators are at the top"
      }, 
      context_instance=RequestContext(request)
  )


@login_required
def admin_indicators_noresources(request):
  indicators = Indicator.objects.filter(resource = None).order_by("added_on")
  return render_to_response (
      'dataexplorer/admin_indicator_list.html',
      { 
        'indicators': indicators, 
        'title': "<em>Admin:</em> Indicators lacking resources", 
        'subtitle': "Oldest indicators are at the top"
      }, 
      context_instance=RequestContext(request)
  )


@login_required
def admin_resources_unlinked(request):
  resources = Resource.objects.filter(url = "").order_by("added_on")
  return render_to_response (
      'dataexplorer/admin_resource_list.html',
      { 
        'resources': resources, 
        'title': "<em>Admin:</em> Resources without links or files", 
        'subtitle': "Oldest resources are at the top"
      }, 
      context_instance=RequestContext(request)
  )


@login_required
def admin_resources_noindicator(request):
  resources = Resource.objects.filter(url = "").order_by("added_on")
  return render_to_response (
      'dataexplorer/admin_resource_list.html',
      { 
        'resources': resources, 
        'title': "<em>Admin:</em> Resources unattached to indicators", 
        'subtitle': "Oldest indicators are at the top"
      }, 
      context_instance=RequestContext(request)
  )


