from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add', addTodo, name='add'),
    path('complete_todo/<todo_id>', completeTodo, name='complete_todo'),
    path('delete_completed', deleteCompleted, name='delete_completed'),
    path('delete_all', deleteAll, name='delete_all'),
]
