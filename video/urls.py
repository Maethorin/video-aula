# -*- coding: utf-8 -*-


from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'land_site.views.home', name='home'),
    url(r'^video-player/', include('video_player.urls')),
)
