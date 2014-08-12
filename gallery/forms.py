# -*- coding: utf-8 -*-
from django import forms
from gallery.models import Photograph


class UploadForm(forms.Form):
    lastname = forms.CharField(max_length=100, label="Nom")
    firstname = forms.CharField(max_length=120, label="Prenom")
    archive = forms.FileField()

    def clean(self):
        cleaned_data = super(UploadForm, self).clean()
        lastname = cleaned_data.get('lastname')
        firstname = cleaned_data.get('firstname')
        return cleaned_data
