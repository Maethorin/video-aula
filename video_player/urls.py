# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
   url(r'^(?P<url_hash>.*)$', 'video_player.views.carregar_video', name='video-player-carregar-video'),
   url(r'^admin/', include(admin.site.urls)),
)
