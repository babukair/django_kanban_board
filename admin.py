from django.contrib import admin
from .models import Board, Product, Task, Status,StatusOrder, TaskStatus, Comment

# Register your models here.
class StatusBoardInline(admin.TabularInline):
    model = StatusOrder
    extra = 0
    
class BoardAdmin(admin.ModelAdmin):
    inlines = [StatusBoardInline]
    
    
class StatusTaskInline(admin.TabularInline):
    model = TaskStatus
    extra = 1
    
class CommentsTaskInline(admin.StackedInline):
    model = Comment
    extra = 1
    
class TaskAdmin(admin.ModelAdmin):
    fieldsets = [("Main", {"fields": (("ref_code", "name",),)}),
                  ("Detail", {"fields": ("description",)}),
                  ("Grouping", {"fields": (("product", "super_task"),)}),
                  ("Numbering", {"fields": (("degree", "priority"),)}),
                 ]
    inlines = [StatusTaskInline, CommentsTaskInline]
    
admin.site.register(Product)
admin.site.register(Board, BoardAdmin)
admin.site.register(Status)
admin.site.register(Task, TaskAdmin)