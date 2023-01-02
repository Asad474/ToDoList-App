from .models import *
from django.forms import *

class TaskForm(ModelForm):
    class Meta:
        model = Task 
        fields = '__all__'
        widgets = { 
            'task' : TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Add new task...'}),
        }