#-*- coding: utf-8 -*-

# Django Framework
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.files.images import ImageFile

# Gallerie
from gallery.models import Photograph, Photo
from gallery.forms import UploadForm

# Other Modules
import shutil, os, zipfile
from PIL import Image

# Create your views here.
def view_content(request):
    return rentder(request, 'gallery/index.html')


