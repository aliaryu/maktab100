from django.shortcuts import render
from account.forms import LoginForm
from task.models import Task
from django.utils import timezone


def index_view(request):
    login_form = LoginForm()
    tasks      = Task.objects.filter(due_date__gte = timezone.now()).order_by("-id")
    context = {
        "login_form": login_form,
        "tasks": tasks
    }
    return render(request, "index.html", context=context)