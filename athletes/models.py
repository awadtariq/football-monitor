from django.db import models

class Player(models.Model):
    player_id = models.CharField(max_length=100, unique=True, help_text="Unique identifier or code for the player")
    name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name or self.player_id

class TrainingLoad(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='training_loads')
    date = models.DateField()
    daily_load = models.FloatField(help_text="Session RPE or training load value")

    def __str__(self):
        return f"{self.player} - {self.date}: {self.daily_load}"