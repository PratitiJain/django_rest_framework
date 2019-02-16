# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils.translation import gettext as _

class Album(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateField(default=datetime.now)

    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    date_created = models.DateField(default=datetime.now)
    album = models.ForeignKey("rest_api.Album", verbose_name=_("album"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Song")
        verbose_name_plural = _("Songs")

    def __str__(self):
        return self.title
