from django import forms
from task.models import CreateTaskModel

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = CreateTaskModel
        fields = ['title','description']
        labels = {
            'title':'Title',
            'description': 'Description'
        }