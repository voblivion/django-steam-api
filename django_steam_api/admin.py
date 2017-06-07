from django.contrib import admin
from steam_api.models import Player


class PlayerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Player, PlayerAdmin)
