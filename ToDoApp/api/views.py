from rest_framework.decorators import api_view
from rest_framework.response import Response
from ToDoApp.models import *
from .serializers import *


@api_view(['GET'])
def apioverview(request):
    routes=[
        'GET /api/',
        'GET /api/tasks/',
        'GET /api/task/:taskid/',
        'GET /api/users/',
        'GET /api/user/:userid/',
    ]
    return Response(routes)


@api_view(['GET'])
def all_tasks(request):
    tasks = Task.objects.all()
    task_serializer = TaskSerializer(tasks, many = True)
    return Response(task_serializer.data)


@api_view(['GET'])
def particular_task(request, pk):
    task = Task.objects.get(id = pk)
    task_serializer = TaskSerializer(task, many = False)
    return Response(task_serializer.data)    


@api_view(['GET'])
def user_task(request, pk):
    user = MyUser.objects.get(id = pk)
    tasks = user.task_set.all()
    task_serializer = TaskSerializer(tasks, many = True)
    return Response(task_serializer.data)    


@api_view(['GET'])
def all_users(request):
    users = MyUser.objects.all()
    user_serializer = UserSerializer(users, many = True)
    return Response(user_serializer.data)