from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTaskForm
from .models import Task


def index(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect("core:index")
    form = NewTaskForm()
    return render(request, "core/index.html", {'form': form})


def complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return render(request, "core/index.html", {'closed': True})
