from django.db import models
from steam_api import managers


class Player(models.Model):
    OFFLINE = 0
    ONLINE = 1
    BUSY = 2
    AWAY = 3
    SNOOZE = 4
    LOOKING_TO_TRADE = 5
    LOOKING_TO_PLAY = 6
    STATE_CHOICES = (
        (OFFLINE, 'Offline'),
        (ONLINE, 'Online'),
        (BUSY, 'Busy'),
        (AWAY, 'Away'),
        (SNOOZE, 'Snooze'),
        (LOOKING_TO_TRADE, 'Looking to trade'),
        (LOOKING_TO_PLAY, 'Looking to play'),
    )

    id = models.CharField(max_length=64, primary_key=True)
    username = models.CharField(max_length=32)
    profile = models.URLField()
    avatar_small = models.URLField()
    avatar_medium = models.URLField()
    avatar_large = models.URLField()
    state = models.IntegerField(choices=STATE_CHOICES, default=OFFLINE)
    is_public = models.BooleanField(default=False)

    objects = managers.PlayerManager()
