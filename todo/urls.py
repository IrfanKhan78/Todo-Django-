from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
	path('', views.home, name = 'home'),
	path('add/', views.add, name = 'add'),
	path('delete/<int:cid>/', views.delete, name = 'delete'),
]