from django.shortcuts import render, redirect
from .models import Task, Category, Tag
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

@login_required
def task_complete(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user)
        task.status = "C"
        task.save()
    except:
        task = None
    if task:
        return redirect("task:task_detail", pk=task.id)
    else:
        context = {
            "error": ["You have no permision for this page.",
                      "Or maybe you ****** *****r kiding us?"]
        }
        return render(request, "404.html", context=context, status=404)

def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        categories = category.tasks.all()
    except:
        categories = None
    if categories:
        context = {
            "category": category,
            "categories": categories
        }
        return render(request, "task/category_detail.html", context=context)
    else:
        context = {
            "error": ["You have no permision for this page.",
                      "Or maybe you ****** *****r kiding us?"]
        }
        return render(request, "404.html", context=context, status=404)

def tag_detail(request, pk):
    try:
        tag = Tag.objects.get(pk=pk)
        tags = tag.tasks.all()
    except:
        tag = None