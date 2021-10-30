from django.db import models

# Create your models here.

class Product(models.Model):
    """Product represent the result which will be achieved on completing task.
        And used to group tasks.
    """
    name = models.CharField(max_length = 140, unique = True)
    description = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return self.name