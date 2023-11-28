from django.shortcuts import render


def index_view(request):

    tasks= 1
    return render(request, "task/index.html", {'tasks': tasks})