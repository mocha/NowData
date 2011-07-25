from django.template import Context
from dataexplorer.models import *
from django.db.models import Count


def sidebar_domains(request):
  domains = Domain.objects.annotate(Count('indicator')).order_by('-indicator__count')[:6]
  return {'sidebar_domains':domains}


def sidebar_counties(request):
  counties = County.objects.all()
  return {'sidebar_counties':counties }