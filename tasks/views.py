from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *
from .forms import *
# Create your views here.

@login_required
def index(request):
    tasks = Task.objects.all().order_by('-id')
    
    form = TaskForm()

   
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
        return redirect('list')

    context = {
        'tasks':tasks,
        'form':form,
        
        
    }
    return render(request,'tasks/list.html', context)

def updateTask(request, pk):

    task = Task.objects.get(id=pk)

    form=TaskForm(instance=task)

    if request.method == 'POST':
         form=TaskForm(request.POST, instance=task)
         if form.is_valid:
            form.save()
            return redirect('list')

    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):

    item = Task.objects.get(id=pk)
    item.delete()
    return redirect('list')


   # if request.method =='POST':
     #   item.delete()
     #   return redirect('list')

   # context = {'item':item}
   # return render(request, 'tasks/delete.html', context)
