
from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    taskAssignDate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )

    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription', 'is_completed', 'taskAssignDate']
