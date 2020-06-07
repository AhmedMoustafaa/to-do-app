from .forms import TodoForm
from .models import *
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.

def todo_list(request):
    tasks = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'tasks': tasks,
        'form': form
    }

    return render(request, 'home.html', context)

def update_item(request, pk):
    task = Todo.objects.get(id=pk)
    form = TodoForm(instance=task)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    
    return render(request, 'item_update.html', context)

def delete_item(request, pk):
    item = Todo.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context = {'item': item}
    return render(request, 'item_delete.html', context)