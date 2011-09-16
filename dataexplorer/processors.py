from django.template import Context
from dataexplorer.models import *
from django.db.models import Count


def sidebar_domains(request):
  # domains = Domain.objects.annotate(Count('indicator')).order_by('-indicator__count')[:6]
  
  domains = Domain.objects.all()
  top_domains = []
  domains_more = []
  i = 1
  
  for domain in domains:
    if i <= 6: top_domains.append(domain)
    else: domains_more.append(domain)
    i = i + 1
  
  return { 
    'sidebar_domains_top' : top_domains, 
    'sidebar_domains_more' : domains_more,
  }


def sidebar_counties(request):
  counties = County.objects.all()
  return {'sidebar_counties':counties }