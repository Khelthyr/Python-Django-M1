from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

from .models import Task
from .forms import TaskForm


def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_tasks = Task.objects.all
            messages.success(request, ('Task has been added'))
            return render(request, 'index.html', {'all_tasks': all_tasks})

    else:
        task_list = Task.objects.all()
        return render(request, 'index.html', {'task_list': task_list})


def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request, ('Item Has Been Deleted!'))
    return redirect('index')


def edit(request, task_id):
    idTask = task_id
    context = {'idTask': idTask}
    return render(request, 'edit.html', context)


# Create your views here.
