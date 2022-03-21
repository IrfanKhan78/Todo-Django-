from django.shortcuts import render, redirect

from .models import Todo
from .forms import TodoForm

import datetime
from pytz import timezone

# Create your views here.
def home(request):
	tz = timezone('GMT')
	date = datetime.datetime.now(tz)

	print(date.time)
	contents = Todo.objects.all()

	context = {'contents' : contents, 'date' : date}

	return render(request, 'todo/home.html', context)

def add(request):
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo:home')
	else:
		form = TodoForm()

	context = {'form' : form}
	return render(request, 'todo/add.html', context)

def delete(request, cid):
	item_to_delete = Todo.objects.get(pk=cid)

	item_to_delete.delete()

	return redirect('todo:home')