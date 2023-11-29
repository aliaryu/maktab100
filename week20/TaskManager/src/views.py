from django.shortcuts import render
from account.forms import LoginForm


def index_view(request):

    login_form = LoginForm()

    context = {
        "login_form": login_form,
    }

    return render(request, "index.html", context=context)