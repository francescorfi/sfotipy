from __future__ import unicode_literals

from django.db import models

#imported relationships
from albums.models import Album
from artists.models import Artist


class Track(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    track_file = models.FileField(upload_to='tracks')
    album = models.ForeignKey(Album, default=0)
    artist = models.ForeignKey(Artist, default=0)
