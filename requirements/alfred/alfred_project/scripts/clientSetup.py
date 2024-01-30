import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'alfred_project.settings'

django.setup()

from django.test import Client
global c
c = Client()

print("use c as a client")
print("call get or post on it to request")
print("ex : c.get(url)")
