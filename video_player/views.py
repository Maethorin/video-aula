from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response


def home(request, url_hash):
    return render_to_response('video_player/home.html')