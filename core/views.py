from django.shortcuts import render, redirect
from .forms import NewTaskForm


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
