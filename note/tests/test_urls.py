from django.test import SimpleTestCase
from django.urls import reverse, resolve
from note.views import HomeView, TodoListView, NoteDetailView, UpdateListView, DeleteListView

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeView)
    
    def test_create_todo_list_url_is_resolved(self):
        url = reverse('create_todo_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TodoListView)
    
    def test_note_detail_url_is_resolved(self):
        url = reverse('note_detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, NoteDetailView)
    
    def test_update_list_url_is_resolved(self):
        url = reverse('update_list', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UpdateListView)
    
    def test_delete_list_url_is_resolved(self):
        url = reverse('delete_list', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, DeleteListView)
    