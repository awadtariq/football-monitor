from django.contrib import admin
from .models import Player, TrainingLoad

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_id', 'name', 'position')
    search_fields = ('player_id', 'name')

@admin.register(TrainingLoad)
class TrainingLoadAdmin(admin.ModelAdmin):
    list_display = ('player', 'date', 'daily_load')
    list_filter = ('date', 'player')
    search_fields = ('player__name', 'player__player_id')