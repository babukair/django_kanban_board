from django.db import models
from .status import Status
from .board import Board

# Create your models here.

class StatusOrder(models.Model):
    """Status order in board.
    """
    board = models.ForeignKey(Board, on_delete = models.CASCADE)
    status = models.ForeignKey(Status, on_delete = models.RESTRICT)
    order = models.PositiveSmallIntegerField()
    
    class Meta:
        ordering = ["board", "order"]
        unique_together = [["board", "status"], ["board", "order"]]
        
    def __str__(self):
        return " / ".join((str(self.board), str(self.status)))
        