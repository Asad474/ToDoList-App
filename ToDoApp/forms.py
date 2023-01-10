from .models import *
from django.forms import *
from django.contrib.auth.forms import *


class TaskForm(ModelForm):
    class Meta:
        model = Task 
        fields = ['task', 'complete']
        widgets = { 
            'task' : TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Add new task...'}),
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser 
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : TextInput(attrs = {'placeholder' : 'Enter Username', 'class' : "form-control form-control-lg"}),
            'email' : EmailInput(attrs = {'placeholder' : 'Enter Email', 'class' : "form-control form-control-lg"}),
        } 

    # In this case, password1 and password2 are declare on the UserCreationForm (they aren't model fields), therefore you can't use them in widgets.    
    def __init__(self, *args, **kwargs) -> None:
        super(SignUpForm,self).__init__(*args, **kwargs)    
        self.fields['password1'].widget = PasswordInput(attrs = {'placeholder' : 'Enter Password', 'class' : "form-control form-control-lg"})
        self.fields['password2'].widget = PasswordInput(attrs = {'placeholder' : 'Enter Confirm Password', 'class' : "form-control form-control-lg"})


class UserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'bio', 'avatar']
        widgets = {
            'username' : TextInput(attrs = {'placeholder' : 'Enter Username', 'class' : "form-control form-control-lg"}),
            'bio' : Textarea(attrs = {'placeholder' : 'Enter about yourself', 'class' : 'form-control form-control-lg'}),
        }