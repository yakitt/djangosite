from django.shortcuts import render,redirect
from .models import Task
from .forms import Taskform
def index(request):
    tasks=Task.objects.order_by('-id')
    return render(request,'main/index.html',{'title': "Главная", 'tasks': tasks})
def about(request):
    return render(request,'main/about.html',{'title': "О сайте"})
def create(request):
    error=''
    if request.method=='POST':
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Форма была неверной'
    form = Taskform()
    return render(request, 'main/create.html', {'form': form,'error': error,'title': "Создать таск"})
