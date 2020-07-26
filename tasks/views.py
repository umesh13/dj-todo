from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
	task = Task.objects.all()
	form =TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context ={
	'task' : task,
	'form' : form
	}
	return render(request,'tasks/list.html',context)


def updateTask(request , pk):
	print("Inside Update Task")
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)
	if request.method == 'POST':
		form = TaskForm(request.POST , instance=task) #Without instance, the date will be saves as new entry
		if form.is_valid:
			form.save()
			return redirect('/')
	
	context = {
	'form' : form
	}
	return render(request,'tasks/update_task.html', context)


def deleteTask(request, pk):
	task = Task.objects.get(id=pk)
	if request.method == 'POST': #IF request is coming from user , delete the item else redirect to render 
		task.delete()
		return redirect('/')
	context ={
	'task' :  task
	}
	return render(request,'tasks/delete.html',context)
