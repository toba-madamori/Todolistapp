from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from note.models import  Todo
from django.urls import reverse_lazy

# Create your views here.


class HomeView(ListView):
    model = Todo
    template_name= 'home.html'    

class TodoListView(CreateView):
    model = Todo
    template_name= 'new_todo_list.html'
    fields= '__all__'

class NoteDetailView(DetailView):
    model = Todo
    template_name= 'note_detail.html'
     