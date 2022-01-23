from django.shortcuts import render, HttpResponseRedirect
from .forms import AddTask
from .models import Task
# Create your views here.

def todo(request):
    if request.method == 'POST':
        fm = AddTask(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['task_name']
            ad = Task(task_name=nm)
            ad.save()
            fm = AddTask()
    else:
        fm = AddTask()
    task1 = Task.objects.all()
    return render(request, 'todo.html', {'form': fm, 'tsk':task1})


def update_data(request, id):
    if request.method == 'POST':
        pi = Task.objects.get(pk=id)
        fm = AddTask(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi = Task.objects.get(pk=id)
        fm = AddTask(instance=pi)
    return render(request, 'updatetask.html', {'form':fm})



# To delete the data 
def delet_data(request, id):
    if request.method=='POST':
        pi = Task.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
