from rest_framework.serializers import ModelSerializer
from ToDoApp.models import * 


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task 
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = MyUser 
        fields = ['id', 'username']