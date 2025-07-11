from django.db import models
from users.models import User

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    leader = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='team_leader')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = ['-created_at']
