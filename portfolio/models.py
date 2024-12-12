# David Alvarado
# CIS 218 
# 12/11/2024

from django.db import models
from django.contrib.auth.models import User
from management.utils import COIN_ID_MAP

class Portfolio(models.Model):
    """ Model for Portfolio """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='portfolio')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Portfolio"

class Holding(models.Model):
    """ Model for Holding """
    
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='holdings')
    coin = models.CharField(max_length=50, choices=[
        (key, key.title()) for key in COIN_ID_MAP.keys()
    ])
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.coin}: {self.quantity}"

    def get_value(self, prices):
        price = prices.get(self.coin.lower(), 0)
        return self.quantity * price
