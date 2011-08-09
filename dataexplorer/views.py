from django.shortcuts import render_to_response
from django.template import RequestContext
from nowdata.dataexplorer.models import *
from django.db.models import Count, Q




def home_page(request):
    return render_to_response (
      'global/home.html', 
      {
        'title': "Welcome <em>to NowData</em>", 
        'subtitle': "Your Resource for Community Data, Now."
      }, 
      context_instance=RequestContext(request)
    )

def about_page(request):
    return render_to_response (
      'global/about.html', 
      {
        'title': "About <em>NowData</em>", 
        'subtitle': "Your Resource for Community Data, Now."
      }, 
      context_instance=RequestContext(request)
    )

def contact_page(request):
    return render_to_response (
      'global/contact.html', 
      {
        'title': "Contact <em>Us</em>", 
        'subtitle': "Your Resource for Community Data, Now."
      }, 
      context_instance=RequestContext(request)
    )

def services_page(request):
    return render_to_response (
      'global/services.html', 
      {
        'title': "Community <em>Services</em>", 
        'subtitle': "Your Resource for Community Data, Now."
      }, 
      context_instance=RequestContext(request)
    )



import operator
def all_indicators(request):
  
  selected_formats = []
  selected_counties = []
  selected_geos = []
  title = ""
  subtitle = ""
  
  
  if request.GET:

    try:
      selected_domain = request.GET['domain']
      domain_filter = Q(domain__slug = selected_domain)
      title = "<em>Exploring:</em> " + Domain.objects.get(slug = selected_domain).name
      
    except: 
      domain_filter = Q()
      selected_domain = ""
      title = "<em>Exploring:</em> All Domains"
    

    try:
      selected_formats = request.GET.getlist('selected_formats')
      format_filter = reduce(operator.or_, [Q(resource__resource_format__slug = str(format)) for format in selected_formats])
      selected_format_subtitle_list = ""
      for format in selected_formats:
        selected_format_subtitle_list = selected_format_subtitle_list + " " + format + ", "
      subtitle = "Including indicators with " + selected_format_subtitle_list
    except: format_filter = Q()


    try: 
      selected_counties = request.GET.getlist('selected_counties')
      county_filter = reduce(operator.or_, [Q(counties__slug = str(county)) for county in selected_counties])      
      selected_county_subtitle_list = ""
      for county in selected_counties:
        selected_county_subtitle_list = selected_county_subtitle_list + " " + County.objects.get(slug=county).name + " County, "
      if subtitle == "":
        subtitle = "Including indicators with " + selected_county_subtitle_list
      else:
        subtitle = subtitle + selected_county_subtitle_list
    except: county_filter = Q()


    try: 
      selected_geos = request.GET.getlist('selected_geos')
      geo_filter = reduce(operator.or_, [Q(levels_of_aggregation__slug = str(geo)) for geo in selected_geos])     
      selected_geo_subtitle_list = ""
      for geo in selected_geos:
        selected_geo_subtitle_list = selected_geo_subtitle_list + " " + Geo_Agg.objects.get(slug=geo).name + ", "
      if subtitle == "":
        subtitle = "Including indicators with " + selected_geo_subtitle_list
      else:
        subtitle = subtitle + selected_geo_subtitle_list 
    except: geo_filter = Q()

    
    indicators = Indicator.objects.filter(
      domain_filter,
      format_filter,
      county_filter,
      geo_filter,
    ).distinct()
    # title = "There's a GET!"
    # subtitle = "It's simply stunning."

  else:
    indicators = Indicator.objects.all()
    title = "<em>Exploring:</em> All Indicators"
    subtitle = "Listing all indicators in our database"
    domain = ""
    format = ""
    county = ""

  all_formats = ResourceFormat.objects.all()
  all_geos = Geo_Agg.objects.all()
  all_domains = Domain.objects.all()

  return render_to_response (
      'dataexplorer/indicator_list.html',
      { 
        'indicators': indicators, 
        'title': title,
        'subtitle': subtitle,
        'all_formats':all_formats,
        'all_geos':all_geos,
        'all_domains':all_domains,
        'selected_domain':selected_domain,
        'selected_formats':selected_formats,
        'selected_counties':selected_counties,
        'selected_geos':selected_geos,
      }, 
      context_instance=RequestContext(request)
  )



import random
def view_indicator(request, slug):
    indicator = Indicator.objects.get(slug = slug)
    related_domain = random.choice(indicator.domain.all())
    related_domain_indicators = related_domain.indicator_set.all()[:6]
    return render_to_response (
        'dataexplorer/view_indicator.html', 
        {
          'indicator': indicator,
          'title': indicator.name,
          'related_domain':related_domain,
          'related_domain_indicators':related_domain_indicators,
        }, 
        context_instance=RequestContext(request)
    )




def all_domains(request):
    domains = Domain.objects.all()
    domains = Domain.objects.annotate(Count('indicator')).order_by('-indicator__count')
    
    return render_to_response (
        'dataexplorer/all_topics.html',
        {
            'domains': domains,
            'title': '<em>Exploring:</em> All Domains',
            'subtitle': "Listing all domains in our database"
        }, context_instance=RequestContext(request)
    )




from django.db.models import Min, Max
def all_years(request):
    year_range = Indicator.objects.exclude(year_start = 0).aggregate(min_year=Min('year_start'), max_year=Max('year_end'))
    years = []
    for n in range(year_range['min_year'], year_range['max_year']):
        years.append(n)
    return render_to_response(
        'dataexplorer/all_years.html',
        { 
          'years': years,
          'title': "<em>Exploring:</em> All Years",
        },
        context_instance=RequestContext(request)
    )




def view_year(request, year):
    indicators = Indicator.objects.filter(year_start__lte = int(year)).filter(year_end__gte = int(year))
    return render_to_response(
        'dataexplorer/indicator_list.html', 
        {
          'indicators':indicators,
          'title': "<em>Indicators covering:</em> " + year, 
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




def admin_indicators_recently_added(request):
  indicators = Indicator.objects.all().order_by("-added_on")
  return render_to_response (
      'dataexplorer/indicator_list.html',
      { 
        'indicators': indicators, 
        'title': "<em>Admin:</em> Recently Added Indicators", 
        'subtitle': "Newest indicators are at the top"
      }, 
      context_instance=RequestContext(request)
  )




def admin_indicators_without_resources(request):
  indicators = Indicator.objects.filter(resource = None).order_by("added_on")
  return render_to_response (
      'dataexplorer/indicator_list.html',
      { 
        'indicators': indicators, 
        'title': "<em>Admin:</em> Indicators lacking Resources", 
        'subtitle': "Oldest indicators are at the top"
      }, 
      context_instance=RequestContext(request)
  )




def admin_indicator_new(request):
  return




def admin_indicator_edit(request):
  return




def admin_indicators_by_status(request, status_code):
  indicators = Indicator.objects.filter(status = status_code).order_by("added_on")
  if status_code == "0": code_name = "Unknown"
  elif status_code == "1": code_name = "Incomplete"
  elif status_code == "2": code_name = "In Progress"
  elif status_code == "3": code_name = "Completed"
  else: code_name = "ERR"
  
  return render_to_response (
      'dataexplorer/indicator_list.html',
      { 
        'indicators': indicators, 
        'title': "<em>Indicators Coded:</em> " + code_name, 
        'subtitle': "Oldest indicators are at the top"
      }, 
      context_instance=RequestContext(request)
  )




def admin_resource_new(request):
  return




def admin_resource_edit(request):
  return




def admin_resources_recently_added(request):
  return




