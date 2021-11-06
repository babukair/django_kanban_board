from django.db import models
from django.contrib.auth.models import User
from .task import Task



class Comment(models.Model):
    comment = models.TextField()
    commenter = models.ForeignKey(User, on_delete = models.CASCADE)
    task = models.ForeignKey(Task, on_delete = models.RESTRICT)
    
    def __str__(self):
        return self.comment[:140] + "..."
    