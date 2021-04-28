from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from note.models import  Todo
from django.urls import reverse_lazy

# Create your views here.


class HomeView(ListView):
    model = Todo
    template_name= 'home.html'    

class TodoListView(CreateView):
    model = Todo
    template_name= 'new_todo_list.html'
    fields= ['title', 'note']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NoteDetailView(DetailView):
    model = Todo
    template_name= 'note_detail.html'
     
class UpdateListView(UpdateView):
    model = Todo
    template_name= 'update_list.html'
    fields= ['title', 'note']
    
class DeleteListView(DeleteView):
    model = Todo
    template_name= 'delete_list.html'
    fields = '__all__'    
    success_url= reverse_lazy('home')