from django.db import models
from users.models import User


class Battle(models.Model):
    player_first = models.ForeignKey(User,  on_delete=models.CASCADE,  null=True, blank=True, related_name='game_user_first')
    player_second = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True, related_name='game_user_second')
    created_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    winner = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'RPS Battle results'

    def __str__(self):
        return 'Status -- ' + self.winner


class Moves(models.Model):
    game_id = models.ForeignKey(Battle, on_delete=models.CASCADE,  null=True, blank=True, related_name='game_moves')
    player_first_move = models.CharField(max_length=50, blank=True)
    player_second_move = models.CharField(max_length=50, blank=True)
    player_first_point = models.PositiveIntegerField(default=100)
    player_second_point = models.PositiveIntegerField(default=100)

    class Meta:
        verbose_name = 'Moves'