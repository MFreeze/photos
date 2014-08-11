# -*- coding: utf-8 -*-

# Gallery Modules
from gallery.models import Photograph, Photo

# Context Processor


def nb_photographs(request):
    return {'nb_pgraph': Photograph.objects.count()}


def nb_photos(request):
    return {'nb_photo': Photo.objects.count()}


def get_pgraphs(request):
    return {'pgraphs': Photograph.objects.all()}



