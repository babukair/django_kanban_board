from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('products/<int:product>/boards/<int:board>', views.kanban_board, name = "board"),
]
