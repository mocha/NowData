import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'NowData.settings'

sys.path.append("/var/www")
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
