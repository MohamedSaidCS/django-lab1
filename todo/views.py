from django.shortcuts import render, redirect

# Create your views here.

todos = [
    {'id': 1, 'name': 'todo 1', 'description': 'Semper eu quis semper congue sollicitudin. Aenean lorem Montes luctus.', 'done': False},
    {'id': 2, 'name': 'todo 2', 'description': 'Nostra sagittis praesent suscipit id congue fames nulla pellentesque orci.', 'done': False},
    {'id': 3, 'name': 'todo 3', 'description': 'Interdum platea morbi. Hymenaeos mus senectus. Nam congue duis aenean.', 'done': False},
    {'id': 4, 'name': 'todo 4', 'description': 'Quam turpis id, rhoncus taciti ante mus pharetra nisi purus.', 'done': False},
]


def index(request):
    return render(request, 'index.html', context={'todos': todos})


def mark_done(request, todo_id):
    todo = list(filter(lambda t: t['id'] == todo_id, todos))[0]
    i = todos.index(todo)
    todos[i]['done'] = True
    return redirect('todo:index')


def create(request):
    return render(request, 'create.html')


def store(request):
    todos.append({
        'id': todos[len(todos) - 1]['id'] + 1 if len(todos) > 0 else 1,
        'name': request.POST['name'],
        'description': request.POST['description'],
        'done': False
    })
    return redirect('todo:index')


def show(request, todo_id):
    todo = list(filter(lambda t: t['id'] == todo_id, todos))[0]
    return render(request, 'show.html', context={'todo': todo})


def edit(request, todo_id):
    todo = list(filter(lambda t: t['id'] == todo_id, todos))[0]
    return render(request, 'edit.html', context={'todo': todo})


def update(request, todo_id):
    todo = list(filter(lambda t: t['id'] == todo_id, todos))[0]
    i = todos.index(todo)
    todos[i]['name'] = request.POST['name']
    todos[i]['description'] = request.POST['description']
    return redirect('todo:index')


def delete(request, todo_id):
    todo = list(filter(lambda t: t['id'] == todo_id, todos))[0]
    i = todos.index(todo)
    todos.pop(i)
    return redirect('todo:index')
