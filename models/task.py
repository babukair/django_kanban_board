from django.db import models
from .product import Product

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length = 140, unique = True)
    description = models.TextField(null = True, blank = True)
    ref_code = models.CharField("Reference Code", max_length = 20)
    degree = models.PositiveSmallIntegerField(null = True, blank = True)
    priority = models.PositiveSmallIntegerField(null = True, blank = True)
    product = models.ForeignKey(Product, on_delete = models.RESTRICT)
    super_task = models.ForeignKey("self", null = True, blank = True, on_delete = models.RESTRICT)
    
    def __str__(self):
        return self.name
    
    
    