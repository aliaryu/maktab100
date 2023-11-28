from django.shortcuts import render


def index_view(request):

    context = 1
    return render(request, "base.html", context)