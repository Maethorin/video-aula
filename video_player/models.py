# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Cliente(models.Model):
    usuario = models.ForeignKey(User)
    ultimo_login = models.DateTimeField()
    conexoes = models.IntegerField()


class HashDeVideoNaoEncontrado(Exception):
    pass


class HashDeVideoExpirado(Exception):
    pass


class Video(models.Model):
    cliente = models.ForeignKey('Video')
    url_hash = models.CharField(max_length=255)
    url_expira_em = models.DateTimeField()
    arquivo = models.CharField(max_length=255)

    def gera_url_hash(self):
        url_hash = str(uuid4()).replace("-", "").upper()
        self.url_hash = url_hash
        self.url_expira_em = datetime.utcnow() + timedelta(days=1),
        self.save()

    def obtem_pelo_hash(self, url_hash):
        try:
            video = Video.objects.get(url_hash=url_hash)
        except Video.DoesNotExist:
            raise HashDeVideoNaoEncontrado(u'Não foi encontrado um vídeo do o hash {}'.format(url_hash))
        if video.url_expira_em < datetime.utcnow():
            raise HashDeVideoExpirado(u'O hash {} para esse vídeo expirou.')
        return video
