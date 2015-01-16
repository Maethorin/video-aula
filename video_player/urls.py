# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
   url(r'^(?P<url_hash>.*)$', 'video_player.views.home', name='video-player-home'),
   url(r'^admin/', include(admin.site.urls)),
)
