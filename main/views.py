from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Home page: shows incomplete and completed tasks
def home(request):
    task = Task.objects.filter(is_completed=False)
    completed = Task.objects.filter(is_completed=True)
    context = {
        'task': task,
        'complete': completed,
    }
    return render(request, 'home-todo.html', context)


# Add new task
def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date') or None
        description = request.POST.get('description')

        Todo = Task.objects.create(
            task=task,
            priority=priority,
            due_date=due_date,
            description=description
        )
        Todo.save()
        return redirect('home')


# Mark task as completed
def mark_as_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True
    task.save()
    return redirect('home')


# Mark task as not completed
def mark_as_undone(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')


# Update task
def update_task(request, update_id):
    get_task = get_object_or_404(Task, id=update_id)

    if request.method == 'POST':
        get_task.task = request.POST.get('new_task')
        get_task.priority = request.POST.get('priority')
        get_task.due_date = request.POST.get('due_date') or None
        get_task.description = request.POST.get('description')
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task
        }
        return render(request, 'update.html', context)


# Delete task
def delete_task(request, delete_id):
    delete_task = get_object_or_404(Task, id=delete_id)
    delete_task.delete()
    return redirect('home')
