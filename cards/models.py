from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone


class Round(models.Model):
    playerId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.CharField(max_length=200)

    gameDate = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.score
