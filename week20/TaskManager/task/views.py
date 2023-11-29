from django.shortcuts import render, redirect
from .models import Task
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user)
    except:
        task = None
    if task:
        context = {
            "task": task
        }
        return render(request, "task/task_detail.html", context=context)
    else:
        context = {
            "error": ["You have no permision for this page.",
                      "Or maybe you ****** *****r kiding us?"]
        }
        return render(request, "404.html", context=context, status=404)

@login_required
def task_delete(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user).delete()
    except:
        task = None
    if task:
        return redirect("index")
    else:
        context = {
            "error": ["You have no permision for this page.",
                      "Or maybe you ****** *****r kiding us?"]
        }
        return render(request, "404.html", context=context, status=404)