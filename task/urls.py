from django.urls import path
from task.views import home, create_task, show_task, delete_task, edit_task
urlpatterns = [
    path('',home),
    path('create_task/',create_task,name='create'),
    path('show_task/', show_task, name="show"),
    path('delete_task/<int:id>', delete_task,name='delete'),
    path('edit_task/<int:id>', edit_task,name="edit"),
]
