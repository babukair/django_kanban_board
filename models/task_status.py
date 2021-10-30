from django.db import models
from .status import Status
from .task import Task
from .board import Board
from .status_order import StatusOrder
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



# Create your models here.

class TaskStatus(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    status = models.ForeignKey(Status, on_delete = models.RESTRICT)
    board = models.ForeignKey(Board, on_delete = models.RESTRICT)
    transfered_on = models.DateTimeField(unique = True)
    taken_by = models.ForeignKey(User, null = True, blank = True,on_delete = models.RESTRICT)
    
    class Meta:
        ordering = ["task", "transfered_on"]
        unique_together = [["task", "transfered_on"]]
        
    def __str__(self):
        return " / ".join((str(self.task), str(self.status), str(self.transfered_on)))
    
#     def save(self, *args, **kwargs):
#         if StatusOrder.objects.filter(status = self.status.pk, board = self.board.pk).exists():
#             return super().save(self, *args, **kwargs)
#         else:
#             raise ValueError('sad')
        
        
    def clean(self):
        super().clean()
        
        if not StatusOrder.objects.filter(status = self.status, board = self.board).exists():
            msg = _("%(status)s is not in %(board)s status")
            params = {"status": self.status, "board": self.board}
            code = "invalid"
            raise ValidationError(msg, params = params, code = code)
