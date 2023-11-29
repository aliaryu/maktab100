from django.shortcuts import render, redirect
from .models import Task, Category, Tag
from django.contrib.auth.decorators import login_required
from account.forms import LoginForm


@login_required
def task_detail(request, pk):
    login_form = LoginForm()
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
                      "Or maybe you ****** *****r kiding us?"],
                      "login_form": login_form
        }
        return render(request, "404.html", context=context, status=404)

@login_required
def task_delete(request, pk):
    login_form = LoginForm()
    try:
        task = Task.objects.get(pk=pk, user=request.user).delete()
    except:
        task = None
    if task:
        return redirect("index")
    else:
        context = {
            "error": ["You have no permision for this page.",
                      "Or maybe you ****** *****r kiding us?"],
                      "login_form": login_form
        }
        return render(request, "404.html", context=context, status=404)

@login_required
def task_complete(request, pk):
    login_form = LoginForm()
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
                      "Or maybe you ****** *****r kiding us?"],
                      "login_form": login_form
        }
        return render(request, "404.html", context=context, status=404)

def category_detail(request, pk):
    login_form = LoginForm()
    try:
        category = Category.objects.get(pk=pk)
        categories = category.tasks.all()
    except:
        categories = None
    if categories:
        context = {
            "category": category,
            "categories": categories,
            "login_form": login_form
        }
        return render(request, "task/category_detail.html", context=context)
    else:
        context = {
            "error": ["You have no permision for this page.",
                      "Or maybe you ****** *****r kiding us?"],
                      "login_form": login_form
        }
        return render(request, "404.html", context=context, status=404)

def tag_detail(request, pk):
    login_form = LoginForm()
    try:
        tag = Tag.objects.get(pk=pk)
        tags = tag.tasks.all()
    except:
        tag = None
    if tag:
        context = {
            "tag": tag,
            "tags": tags,
            "login_form": login_form
        }
        return render(request, "task/tag_detail.html", context=context)
    else:
        context = {
            "error": ["You have no permision for this page.",
                      "Or maybe you ****** *****r kiding us?"],
                      "login_form": login_form
        }
        return render(request, "404.html", context=context, status=404)

@login_required
def mine(request):
    login_form = LoginForm()
    mine = Task.objects.filter(user_id=request.user.id)
    return render(request, "task/mine.html", context={"mine":mine, "login_form": login_form})

def categories(request):
    login_form = LoginForm()
    categories = Category.objects.all()
    return render(request, "task/categories.html", context={"categories":categories, "login_form": login_form})

def search(request):
    login_form = LoginForm()
    param = request.GET["search"].strip()
    if len(param) <= 0:
        return render(request, "task/search.html", context={"login_form": login_form})
    if param[0] == "#":
        tasks = Task.objects.filter(tags__tag__icontains=param[1:])
    else:
        tasks = Task.objects.filter(title__icontains=param)
    return render(request, "task/search.html", context={"tasks": tasks, "login_form": login_form})