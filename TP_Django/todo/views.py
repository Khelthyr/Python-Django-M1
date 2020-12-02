from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Task


def index(request):
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        label_content = request.POST.get('content')
        task = Task.objects.create(
            content=label_content
        )
        return render(request, 'index.html')


# def edit(request, task_id):
#     idTask = task_id
#     context = {'idTask': idTask}
#     return render(request, 'edit.html', context)


# Create your views here.
