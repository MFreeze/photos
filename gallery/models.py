#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Photograph(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    
    def __unicode__(self):
        return u"" + self.firstname + " " + self.lastname
    
class Photo(models.Model):
    author = models.ForeignKey('Photograph')
    med_thumb = models.ImageField(upload_to="photos/")
    small_thumb = models.ImageField(upload_to="photos/")

    def __unicode__(self):
        return u"%s" % self.med_thumb.name
