from django.shortcuts import render, redirect
from .models import Profile, Todo
from .forms import RegisterFormClass, TodoFormClass, TodoFormUpdateClass
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.

def SignUpView(request):
    form = RegisterFormClass(request.POST or None)
    if request.method == 'POST':
        form = RegisterFormClass(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data['username']

            user = form.save()

            profile = Profile.objects.create(
                created_by=user,
                name=user.username
            )
            
            messages.success(request, f'New account has been created for {username} successfully!')
            
            return redirect('success_signup')
        else:
            messages.error(request, 'Something went wrong!')

    context = {
        'form':form
    }

    return render(request, 'todo/register.html', context)

def SignUpSucessView(request):
    return render(request, 'todo/success_signup.html')

def index(request):
    todos = Todo.objects.order_by('-updated_at')

    context = {'todos':todos}
    return render(request, 'todo/index.html', context)

def CreateTodoView(request):
    if request.method == 'POST':
        form = TodoFormClass(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user.profiles
            instance.save()
            messages.success(request, f'You have successfully added a new todo!')
            return redirect('index')
        else:
            messages.error(request, 'Something went wrong!')
    
    form = TodoFormClass()
    return render(request, 'todo/create_todo.html', {'form':form})

def UpdateTodoView(request, pk):
    queryset = Todo.objects.get(id=pk)
    form = TodoFormUpdateClass(instance=queryset)
    
    if request.method == 'POST':
        form = TodoFormUpdateClass(request.POST, instance=queryset)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Todo has been updated!")
            return redirect('index')
        
        else:
            messages.error(request, 'Something went wrong!')

    context = {'queryset':queryset, 'form':form}
    return render(request, 'todo/update_todo.html', context)

def DeleteTodoView(request, pk):
    queryset = Todo.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('index')
    return render(request, 'todo/delete_todo.html', {'queryset':queryset})