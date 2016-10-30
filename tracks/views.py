from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Track
import json

def track_view(request, title):
    track = get_object_or_404(Track, title=title)
    bio = track.artist.biography

    data = {
        'title': track.title,
        'order': track.order,
        'album': track.album.title,
        'artist': {
            'name': track.artist.first_name,
            'bio': bio
        }
    }

    # to convert a python dictionary to a json:
    json_data = json.dumps(data)

    #in case we wanted to convert from json to a Python dictionary:
    # json.loads(_String in json_)

    return HttpResponse(json_data, content_type='application/json')

    # return render(request, 'track.html', {'track': track})
