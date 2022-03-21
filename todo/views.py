from django.shortcuts import render, redirect

from .models import Todo
from .forms import TodoForm

import datetime

# Create your views here.
def home(request):
	date = datetime.datetime.now()

	month = date.month
	year = date.year
	day = date.day

	print(date.time)
	contents = Todo.objects.all()

	context = {'contents' : contents, 'day' : day, "month": month, "year": year}

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