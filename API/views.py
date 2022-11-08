from turtle import title
from django.shortcuts import render,redirect
from django.http import HttpResponse , JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404
from .forms import createnewtask

#de prueba
# {% extends 'base.html' %}


def iniciomatch(request):
    bienvenidoamatch= 'somos match'
    return render(request, 'matchprincipal.html',{
        'matchprincipal': bienvenidoamatch
    })

def hola(request):
    return HttpResponse("hola chavales")
def index(request):
    title='bienvenido a curso django ¡¡ '
    return render(request,'index.html',{
        'title':title
    })

def about(request):
    username ='Juan Rojas'
    return render(request,'about.html',{
        'username': username
    })
    
#esta funcion con params lo muestra por consola el nombre ingresado
def hello(request, id):
    result = int(id +100 *2)
    return HttpResponse("<h2>hola con paramas %s<h2>" % result)

#con esta funcion obtenemos los proyectos
def project(request):
    project = Project.objects.all()
    return render(request, 'projects.html',{
        'projects':project
    })


#con esta funcion obtenemos las tareas
def task(request, id):
    #task=Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task %s' % task.title)


 #print(request.GET['title'])
    #print(request.GET['description'])
    #Task.objects.create(title=request.GET['title'],description=request.GET['description'],Project=2)
    # return render(request,'create_task.html',{
    #   'form': createnewtask()
    #   })



def create_task(request):
    if request.method =='GET':
        return render(request,'create_task.html',{
        'form': createnewtask()}
        )
    else:
        Task.objects.create(title=request.POST['title'],description=request.POST['description'],Project=2)
        return redirect('project')
