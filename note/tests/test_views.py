from django.test import TestCase, Client
from note.views import HomeView, TodoListView, NoteDetailView, UpdateListView, DeleteListView
from django.urls import reverse
from note.models import Todo
import json



