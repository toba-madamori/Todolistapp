from django.urls import path
from note.views import HomeView, TodoListView, NoteDetailView, UpdateListView, DeleteListView

urlpatterns = [
    #path('', views.home, name= 'home'),
    path('', HomeView.as_view(), name= 'home'),
    path('create_todo_list/', TodoListView.as_view(), name= 'create_todo_list'),
    path('note_detail/<int:pk>', NoteDetailView.as_view(), name= 'note_detail'),
    path('update_list/<int:pk>', UpdateListView.as_view(), name= 'update_list'),
    path('delete_list/<int:pk>', DeleteListView.as_view(), name= 'delete_list'),

    
]
