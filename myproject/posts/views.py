from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForms
# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'posts/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForms()
    return render(request, 'posts/task_form.html', {'form': form})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')