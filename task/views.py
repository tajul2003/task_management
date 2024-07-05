
from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskForm
from category.models import TaskCategory

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        categories = request.POST.getlist('categories')
        if form.is_valid():
            task = form.save()
            task.categories.set(categories)
            return redirect('show_tasks')
    else:
        form = TaskForm()
        categories = TaskCategory.objects.all()
    return render(request, 'add_task.html', {'form': form, 'categories': categories})

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        categories = request.POST.getlist('categories')
        if form.is_valid():
            task = form.save()
            task.categories.set(categories)
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
        categories = TaskCategory.objects.all()
        selected_categories = task.categories.all().values_list('id', flat=True)
    return render(request, 'edit_task.html', {
        'form': form,
        'categories': categories,
        'selected_categories': selected_categories
    })

def delete_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    task.delete()
    return redirect('show_tasks')

def complete_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')
