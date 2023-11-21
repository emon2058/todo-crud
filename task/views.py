from django.shortcuts import render, redirect
from django.http import HttpResponse
from task.forms import CreateTaskForm
from task.models import CreateTaskModel
# Create your views here.
def home(request):
    return HttpResponse('welcome')

def create_task(request):
    if request.method == 'POST':
        task = CreateTaskForm(request.POST)
        if task.is_valid():
            print(task.cleaned_data)
            task.save()
            return redirect('show')
    else:
        task = CreateTaskForm()
    return render(request,'create_task.html',{'form':task})

def show_task(request):
    tasks = CreateTaskModel.objects.all()
    return render(request,'show_task.html',{'tasks':tasks})

def delete_task(request,id):
    task = CreateTaskModel.objects.get(pk=id).delete()
    return redirect('show')

def edit_task(request,id):
    task_model = CreateTaskModel.objects.get(pk=id)
    task_form = CreateTaskForm(instance = task_model)
    if request.method == "POST":
        update_task = CreateTaskForm(request.POST, instance = task_model)
        if update_task.is_valid():
            update_task.save()
            return redirect('show')
        
    return render(request,'create_task.html',{'form':task_form})