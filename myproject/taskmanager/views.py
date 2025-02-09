from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .forms import TaskForm
from .models import *


def task_list(request):
    tasks = Task.objects.all()
    return render (request, 'taskmanager/task_list.html',{'tasks':tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render (request, 'taskmanager/task_form.html',{'form':form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Get the task or return 404

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Bind form with existing task
        if form.is_valid():
            form.save()  # Save updated task
            return redirect('task_list')  # Redirect to task list after update
    else:
        form = TaskForm(instance=task)  # Prepopulate form with task data

    return render(request, 'taskmanager/task_update.html', {'form': form, 'task': task})




def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Ensure task exists or return 404
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Redirect after deleting
    return render(request, 'taskmanager/task_delete.html', {'task': task})