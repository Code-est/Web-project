from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from .forms import RegisterUserForm


def index(request):
    tasks = Task.objects.all()
    return render(request, "main/index.html", {"title" : "Главная страница сайта", "tasks" : tasks})

def about(request):
    return render(request, "main/about-us.html")

def create(request):
    error = ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу
        else:
            error = "Форма была неверной"  # Сообщение об ошибке

    form = TaskForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, "main/create.html", context)

def secret(request):
    return render(request, template_name= "main/secret.html")

def login(request):
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")

        usr = authenticate(request, username=login, password=password)
        if usr is not None:
            user_login(request, usr)
            return HttpResponseRedirect("secret")
        else:
            return render(request, template_name= "main/login.html")

    return render(request, template_name= "main/login.html")

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return render(request, "main/secret.html")
    else:
        form = RegisterUserForm()

    return render(request, "main/register.html", {"form": form})

def logout(request):
    user_logout(request)
    return HttpResponseRedirect("login")
