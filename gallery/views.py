# -*- coding: utf-8 -*-

# Django Framework
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.files.images import ImageFile

# Gallerie
from gallery.models import Photograph, Photo
from gallery.forms import UploadForm

# Other Modules
import shutil
import os
import zipfile

from PIL import Image

# Create your views here.


def view_content(request):
    return render(request, 'gallery/index.html')


def handle_uploaded_file(f, upload_auth):
    with open(settings.MEDIA_ROOT + str(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    arc = zipfile.ZipFile(
        settings.MEDIA_ROOT + "77_toutes_photos.zip", "a",
        zipfile.ZIP_DEFLATED)
    before = os.listdir(settings.MEDIA_ROOT)
    try:
        shutil.unpack_archive(
            settings.MEDIA_ROOT + str(f),
            extract_dir=settings.MEDIA_ROOT)
    except Exception as e:
        os.remove(settings.MEDIA_ROOT + str(f))
        raise Exception(e)
    after = os.listdir(settings.MEDIA_ROOT)
    diff = [fpath for fpath in after if fpath not in before]

    for i in diff:
        path = settings.MEDIA_ROOT + i
        im_name = upload_auth.firstname + "_" + upload_auth.lastname + "_" + i
        mid_thumb = "m_" + im_name
        small_thumb = "s_" + im_name
        # Create Thumbnails
        tmp_pict = Image.open(path)
        ratio = max(tmp_pict.size[0] / 950, tmp_pict.size[1] / 712)
        tmp_pict.thumbnail(
            tuple([int(x / ratio) for x in tmp_pict.size]), Image.ANTIALIAS)
        tmp_pict.save(mid_thumb, tmp_pict.format)
        tmp_pict.close()

        tmp_pict = Image.open(path)
        ratio = max(tmp_pict.size[0] / 130, tmp_pict.size[1] / 98)
        tmp_pict.thumbnail(
            tuple([int(x / ratio) for x in tmp_pict.size]), Image.ANTIALIAS)
        tmp_pict.save(small_thumb, tmp_pict.format)
        tmp_pict.close()

        # Create an Photo instance
        photo = Photo(author=upload_auth)
        photo.med_thumb.save(mid_thumb, ImageFile(open(mid_thumb, 'rb')))
        photo.small_thumb.save(small_thumb, ImageFile(open(small_thumb, 'rb')))
        photo.save()

        os.rename(path, settings.MEDIA_ROOT + im_name)
        arc.write(settings.MEDIA_ROOT + im_name)
        os.remove(settings.MEDIA_ROOT + im_name)
        os.remove(mid_thumb)
        os.remove(small_thumb)
    os.remove(settings.MEDIA_ROOT + str(f))
    arc.close()


def view_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            lastname = form.cleaned_data['lastname']
            firstname = form.cleaned_data['firstname']
            try:
                upload_auth = Photograph.objects.get(
                    lastname=lastname, firstname=firstname)
            except Exception as e:
                upload_auth = Photograph(
                    lastname=lastname, firstname=firstname)
                upload_auth.save()
            try:
                handle_uploaded_file(request.FILES['archive'], upload_auth)
            except Exception as e:
                print(e)
    else:
        form = UploadForm()
    return render(request, 'gallery/upload.html', locals())


def view_gallery(request, pgraph_id):
    desired_aut = get_object_or_404(Photograph, id=pgraph_id)
    photos = Photo.objects.filter(author=desired_aut)
    if len(photos):
        main_pic = photos[0]
    return render(request, 'gallery/gallery.html', locals())


def view_photo(request, pgraph_id, photo_id):
    desired_aut = get_object_or_404(Photograph, id=pgraph_id)
    photos = Photo.objects.filter(author=desired_aut)
    if photos:
        main_pic = photos[0]
    for i in photos:
        if (str(i.id) == str(photo_id)):
            main_pic = i

    return render(request, 'gallery/gallery.html', locals())


def view_list_pgraphs(request):
    return render(request, 'gallery/all_pgraphs.html', locals())
