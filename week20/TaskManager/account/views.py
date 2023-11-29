from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
# from django.views.decorators.http import require_POST
from django.http import HttpResponse


def login_view(request):
    login_form = LoginForm
    if request.method == "POST":
        login_form = login_form(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("index")
    return render(request, "account/login.html", context={"login_form": login_form})


def logout_view(request):
    logout(request)
    return redirect("index")
