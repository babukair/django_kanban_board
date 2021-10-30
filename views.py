from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F, Max

from .models import Board, Product, Task, Status, TaskStatus

# Create your views here.

def index(request):
    context = {"products": Product.objects.all(), "boards": Board.objects.all()}
    return render(request, "kanban_board/choose_board.html", context)

def kanban_board(request, product, board):
    try:
        board = Board.objects.get(pk = board)
        statusorder = board.statusorder_set.all()
        tasks = (Task.objects.filter(product = product , taskstatus__board = board)
                 .annotate(last_transfered_on =  Max("taskstatus__transfered_on"))
                 .filter(taskstatus__transfered_on = F("last_transfered_on"))
                 .values("pk", "name", "degree", "description", "priority",
                         "product", "ref_code", "super_task__name",
                         "taskstatus__status", "taskstatus__taken_by__username",
                         "taskstatus__transfered_on")
                 )
        tasks_list = []
        
        for s in statusorder:
            tasks_list.append([])
            for t in tasks:
                if t["taskstatus__status"] == s.status.pk:
                    tasks_list[-1].append(t)
                    
        return render(request, "kanban_board/board.html", {"status": statusorder, "tasks_list": tasks_list})
    
    except ObjectDoesNotExist as err:
        raise Http404(err)
