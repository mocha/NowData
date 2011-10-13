from django.template import Context
from dataexplorer.models import *
from django.db.models import Count


def sidebar_domains(request):
  domains = Domain.objects.exclude(id=99).annotate(indicator_count = Count('domaingroup__indicator')).order_by('-indicator_count')
  return { 'sidebar_domains' : domains, }


def sidebar_counties(request):
  counties = County.objects.all()
  return {'sidebar_counties':counties }