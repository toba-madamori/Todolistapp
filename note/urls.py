from django.urls import path
from note.views import HomeView, TodoListView, NoteDetailView

urlpatterns = [
    #path('', views.home, name= 'home'),
    path('', HomeView.as_view(), name= 'home'),
    path('create_todo_list/', TodoListView.as_view(), name= 'create_todo_list'),
    path('note_detail/<int:pk>', NoteDetailView.as_view(), name= 'note_detail'),

    
]
