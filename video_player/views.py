# -*- coding: utf-8 -*-
import os

from django.shortcuts import render_to_response
from video_player.models import Video, VideoNaoEncontrado


def carregar_video(request, url_hash):

    try:
        video = Video.obtem_pelo_hash(url_hash)
    except VideoNaoEncontrado:
        return render_to_response('video_player/carregar-video.html', {'video': None, 'erro': u'Vídeo não encontrado.'})

    buf_size = 1024 * 5
    f = open(video, 'rb')
    size = os.path.getsize(video)
    def stream():
        data = f.read(buf_size)
        while len(data) > 0:
            yield data
            data = f.read(buf_size)

    return render_to_response('video_player/carregar-video.html', {'video': video})

