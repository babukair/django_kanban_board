from django.urls import path
from . import views

app_name = "django_kanban_board"

urlpatterns = [
    path('', views.index, name = "index"),
    path('products/<int:product>/boards/<int:board>', views.kanban_board, name = "board"),
    path('products/add_comment', views.add_comment, name = "add_comment"),
]
