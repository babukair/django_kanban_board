from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import F, Max
from django.contrib import auth
from django.core.exceptions import PermissionDenied

from .models import Board, Product, Task, Comment

# Create your views here.

def index(request):
    context = {"products": Product.objects.all(), "boards": Board.objects.all()}
    return render(request, "kanban_board/choose_board.html", context)

def kanban_board(request, product, board):
    board = get_object_or_404(Board, pk = board)
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
                t["comments"] = Comment.objects.filter(task = t["pk"])
                tasks_list[-1].append(t)
                
    return render(request, "kanban_board/board.html", {"status": statusorder, "tasks_list": tasks_list})



    
def add_comment(request):
    user = auth.get_user(request)
    if user.is_anonymous:
        raise PermissionDenied("Hello")
    else:
        if "comment" in request.POST and request.POST["comment"]:
            task = get_object_or_404(Task, pk = request.POST["task"])
            task.comment_set.create(comment = request.POST["comment"], commenter = user)
            
        if "prev_url" in request.POST and request.POST["prev_url"]:
            return HttpResponseRedirect(request.POST["prev_url"])
        else:
            return HttpResponseRedirect("/")
        
