from django.shortcuts import render , redirect
from .models import *
from .forms import * 

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'tasks':tasks , 'form':form}
    return render(request, 'ToDoApp/home.html', context)


def updatetask(request,pk):
    task = Task.objects.get(id = pk)
    tasks = Task.objects.all()
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'tasks':tasks , 'form':form}
    return render(request, 'ToDoApp/home.html', context)


def deletetask(request,pk):
    obj = Task.objects.get(id = pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')

    context = {'obj':obj}
    return render(request, 'ToDoApp/delete.html', context)