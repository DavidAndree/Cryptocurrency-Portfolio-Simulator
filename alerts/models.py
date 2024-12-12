# David Alvarado
# CIS 218 
# 12/11/2024

from django.db import models
from django.contrib.auth.models import User 

class Alert(models.Model):
    """ Model for Alert """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.CharField(max_length=50) 
    price_threshold = models.FloatField()  
    direction = models.CharField(
        max_length=4,
        choices=[('UP', 'Above'), ('DOWN', 'Below')],
        default='UP'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    triggered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.coin} - {self.price_threshold} ({self.direction})"