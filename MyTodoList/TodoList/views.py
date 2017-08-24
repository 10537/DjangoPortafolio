from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    TodoList = Todo.objects.all()
    context = {
        'Todos': TodoList,
    }
    return render(request, "index.html", context)


def details(request, detail_id):
    TodoDetail = Todo.objects.get(id=detail_id)
    context = {
        'Todo': TodoDetail,
    }
    return render(request, "details.html", context)


def new(request):
    if request.method != 'POST':
        return render(request, 'new.html')

    title = request.POST['title']
    text = request.POST['text']
    state = request.POST['state']

    new_todo = Todo(title=title, text=text, state=state)
    new_todo.save()

    return redirect('/')
