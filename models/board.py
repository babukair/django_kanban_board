from django.db import models

# Create your models here.

class Board(models.Model):
    """Board to order status.
    """
    name = models.CharField(max_length = 140, unique = True)
    description = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return self.name