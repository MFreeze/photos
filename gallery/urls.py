#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns ('gallery.views',
        url('^$', 'view_content', name='accueil'),
        url('^upload/$', 'view_upload', name='upload'),
        url(r'^(?P<pgraph_id>\d+/$', 'view_gallery', name='pgraph_gal'),
        url(r'^(?P<pgraph_id>\d+)/(?P<photo_id>\d+)/$', 'view_gallery', name='photo_gal'),
)
