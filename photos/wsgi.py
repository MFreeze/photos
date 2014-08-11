"""
WSGI config for photos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "photos.settings")
# 
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
import site 
import sys 
import os 
DIRS = [‘/PATH_VERS_VOTRE_VIRTUALENV/lib/VOTRE_VERSION_PYTHON/site-packages’] 
      
for directory in DIRS: 
    site.addsitedir(directory) 
    sys.path.insert(0,directory) 
            
root = os.path.join(os.path.dirname(__file__)) 
  
sys.path.insert(0,root) 
os.environ[‘DJANGO_SETTINGS_MODULE’]=’settings’ 

import django.core.handlers.wsgi 
application = django.core.handlers.wsgi.WSGIHandler()

