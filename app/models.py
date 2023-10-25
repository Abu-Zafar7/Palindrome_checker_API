from django.db import models


class Game(models.Model):
    board = models.CharField(max_length=10)
    is_palindrome = models.BooleanField(default=False)
    
