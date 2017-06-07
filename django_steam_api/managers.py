from django.db import models
from django.conf import settings
import requests


class SteamManager(models.Manager):
    base_url = 'http://api.steampowered.com/'

    def steam_query(self, url, params={}):
        params['key'] = settings.STEAM_API_KEY
        raw_data = requests.get(url, params)
        data = raw_data.json()
        return data['response']


class PlayerManager(SteamManager):
    player_url = SteamManager.base_url + 'ISteamUser/GetPlayerSummaries/v0002/'

    def steam_create(self, steam_id):
        raw_data = self.steam_query(self.player_url, {'steamids': steam_id})
        raw_data = raw_data['players'][0]
        data = {
            'id': raw_data['steamid'],
            'username': raw_data['personaname'],
            'profile': raw_data['profileurl'],
            'avatar_small': raw_data['avatar'],
            'avatar_medium': raw_data['avatarmedium'],
            'avatar_large': raw_data['avatarfull'],
            'state': raw_data['personastate'],
            'is_public': raw_data['communityvisibilitystate'] == 3,
        }
        return self.create(**data)
