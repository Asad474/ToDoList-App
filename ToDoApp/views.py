from django.shortcuts import render , redirect
from .models import *
from .forms import * 
from .decorators import * 
from ToDoList import settings
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden

# Create your views here.
@login_required(login_url = 'loginuser')
def home(request):
    user = request.user
    # tasks = user.task_set.all()
    tasks = Task.objects.filter(user = user)

    tk = request.GET.get('task') if request.GET.get('task') else ''
    completed = request.GET.get('completed') if request.GET.get('completed') else ''

    if len(tk) > 0 and len(completed) > 0: 
        tasks = Task.objects.filter(user = user, task = tk, complete = completed)

    elif len(tk) > 0:
        tasks = Task.objects.filter(user = user, task = tk)

    elif len(completed) > 0:
        tasks = Task.objects.filter(user = user, complete = completed)    

    pending_tasks_count = user.task_set.filter(complete = False).count()
    total = tasks.count()
    form = TaskForm()

    if request.method == 'POST':
        u = request.user
        t = request.POST.get('task')

        if {'task' : t} in tasks.values('task'):
            messages.warning(request, 'This task already exists!!!')

        else:    
            task = Task(user = u, task = t)
            task.save()

        return redirect('home')

    context = {
        'user' : user,
        'tasks' : tasks,
        'form' : form,
        'pending_tasks_count' : pending_tasks_count,
        'total' : total,    
    }

    return render(request, 'ToDoApp/home.html', context)


@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = authenticate(request, email = email, password = password)
            login(request,user)
            return redirect('home')

        except:
            messages.error(request, 'Email or Password is invalid!!!')

    return render(request,'ToDoApp/signin.html')


def logoutpage(request):
    logout(request)    
    return redirect('home')


@unauthenticated_user
def registeruser(request):
    form = SignUpForm()

    try:
        if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid:                
                user = form.save()
                subject = 'Welcome to ToDoListApp!!!'
                mesg = f'Hi {user.username}, thank you for registering!!!'
                host_email = settings.EMAIL_HOST_USER
                user_email_list = [user.email,]
                send_mail(subject, mesg, host_email, user_email_list)
                messages.success(request, f'Hi {user.username}, thank you for registering!!!')
                return redirect('loginuser')

    except:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        all_users_username = MyUser.objects.all().values('username')
        all_users_email = MyUser.objects.all().values('email')

        if {'username' : username} in all_users_username:
            messages.error(request, f'User with username "{username}" already exists!!!')

        if {'email' : email} in all_users_email:
            messages.error(request, 'User with this email id already exists!!!')    

        if password1 != password2:
            messages.error(request ,'Password and Confirm Password are not matching with each other!!!')

        else:
            messages.error(request ,'Something went wrong!!!')    

        return redirect('registeruser')

    context={'form' : form}
    return render(request,'ToDoApp/signup.html',context)


@login_required(login_url = 'loginuser')
def updatetask(request,pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance = task)

    if request.user.id != task.user.id:
        return HttpResponseForbidden('You are not authorized to access this page !!!')

    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'ToDoApp/update.html', context)


@login_required(login_url = 'loginuser')
def deletetask(request,pk):
    obj = Task.objects.get(id = pk)

    if request.user.id != obj.user.id:
        return HttpResponseForbidden('You are not authorized to access this page !!!')

    if request.method == 'POST':
        obj.delete()
        return redirect('home')

    context = {'obj':obj}
    return render(request, 'ToDoApp/delete.html', context)


@login_required(login_url = 'loginuser')
def userprofile(request,pk):
    u = MyUser.objects.get(id = pk)   

    if request.user.id != u.id:
        return HttpResponseForbidden('You are not authorized to access this page !!!')

    context = {'u' : u}
    return render(request,'ToDoApp/user_profile.html',context)


@login_required(login_url = 'loginuser')    
def updateprofile(request):
    user = request.user
    form = UserForm(instance = user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'u' : user, 'form' : form}
    return render(request, 'ToDoApp/userform.html', context)        
