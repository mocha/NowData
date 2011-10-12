from django.template import Context
from dataexplorer.models import *
from django.db.models import Count


def sidebar_domains(request):

  domains = Domain.objects.exclude(id=99).annotate(indicator_count = Count('domaingroup__indicator')).order_by('-indicator_count')
  
  top_domains = []
  domains_more = []
  i = 1
  
  for domain in domains:
    if domain.indicator_count > 0:
      if i <= 4: top_domains.append(domain)
      else: domains_more.append(domain)
      i = i + 1
  
  return { 
    'sidebar_domains_top' : top_domains, 
    'sidebar_domains_more' : domains_more,
  }


def sidebar_counties(request):
  counties = County.objects.all()
  return {'sidebar_counties':counties }