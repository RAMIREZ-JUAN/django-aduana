from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from .forms import ScanForm, CpuForm, MonForm, LapForm, DiskForm
from django.views.generic import ListView

from django.http import HttpResponse
from fpdf import FPDF


# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})


@login_required
def tasks(request):
    tasks = Task.objects.filter(
        user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {"tasks": tasks})


@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(
        user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {"tasks": tasks})


@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {"form": TaskForm, "error": "Error creating task."})


@login_required
def create_scan(request):
    if request.method == "GET":
        return render(request, 'create_scan.html', {"form": ScanForm})
    else:
        try:
            form = ScanForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_scan.html', {"form": ScanForm, "error": "Error creating task."})


@login_required
def create_cpu(request):
    if request.method == "GET":
        return render(request, 'create_cpu.html', {"form": CpuForm})
    else:
        try:
            form = CpuForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_cpu.html', {"form": CpuForm, "error": "Error creating task."})


@login_required
def create_monitor(request):
    if request.method == "GET":
        return render(request, 'create_monitor.html', {"form": MonForm})
    else:
        try:
            form = MonForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_monitor.html', {"form": MonForm, "error": "Error creating task."})


@login_required
def create_lap(request):
    if request.method == "GET":
        return render(request, 'create_lap.html', {"form": LapForm})
    else:
        try:
            form = LapForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_lap.html', {"form": LapForm, "error": "Error creating task."})


@login_required
def create_disco(request):
    if request.method == "GET":
        return render(request, 'create_disco.html', {"form": DiskForm})
    else:
        try:
            form = DiskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_disco.html', {"form": DiskForm, "error": "Error creating task."})


def home(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicio.html')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Usuario o contraseña incorrecta."})

        login(request, user)
        return redirect('home')


@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task.'})


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')


class ForMantenimiento(ListView):
    model = Task
    template_name = "mante.html"
    context_object_name = 'tasks'


def generar_pdf(request):
    # Crear una instancia del objeto FPDF
    pdf = FPDF()

    # Agregar una página
    pdf.add_page()

    # Establecer el tipo de letra y el tamaño
    pdf.set_font("Arial", size=10)

    # Título del reporte
    image_path = "tasks/static/app/images/aduana.png"
    pdf.image(image_path, x=10, y=10, w=55, h=15) 

    pdf.multi_cell(w=0, h=15, txt='FORMULARIO DE MANTENIMIENTO', border=1,
                align='C', fill=0)
    pdf.multi_cell(w=0, h=8, txt='', border=1,
                align='C', fill=0)
    pdf.multi_cell(w=0, h=10, txt='A. DATOS GENERALES', border=1,
                align='C', fill=0)
    h_sep=8
    pdf.cell(w=45, h=h_sep, txt='NOMBRE', border=1,
            align='C', fill=0)
    pdf.multi_cell(w=0, h=h_sep, txt='', border=1,
                align='C', fill=0)

    pdf.cell(w=45, h=h_sep, txt='UNIDAD', border=1,
            align='C', fill=0)
    pdf.multi_cell(w=0, h=h_sep, txt='', border=1,
                align='C', fill=0)

    pdf.cell(w=45, h=h_sep, txt='CODIGO DE ACTIVO', border=1,
            align='C', fill=0)
    pdf.multi_cell(w=0, h=h_sep, txt='', border=1,
            align='C', fill=0)

    pdf.cell(w=45, h=h_sep, txt='FECHA', border=1,
            align='C', fill=0)
    pdf.multi_cell(w=0, h=h_sep, txt='', border=1,
            align='C', fill=0)

    pdf.multi_cell(w=0, h=h_sep, txt='MANTENIMIENTO DE HARDAWARE', border=1,
                align='C', fill=0)
    
    pdf.cell(w=15, h=h_sep, txt='Nro', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='ACTIVIDAD', border=1,
                align='C', fill=0)
    pdf.cell(w=87, h=h_sep, txt='TRABAJO REALIZADO', border=1,ln=1,
                align='C', fill=0)
    #1
    pdf.cell(w=15, h=h_sep, txt='1', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='SOPLETEAR LA PC', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt='', border=1,ln=1,
                align='C', fill=0)
    #2
    pdf.cell(w=15, h=h_sep, txt='2', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='SOPLETEAR LA FUENTE DE PODER', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt=' ', border=1,ln=1,
                align='C', fill=0)
    #3
    pdf.cell(w=15, h=h_sep, txt='3', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='LIMPIAR EL GABINETE DE LA PC', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt='', border=1,ln=1,
                align='C', fill=0)
    #4
    pdf.cell(w=15, h=h_sep, txt='4', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='SOPLETEAR EL TECLADO Y MOUSE', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt='', border=1,ln=1,
                align='C', fill=0)
    #5
    pdf.cell(w=15, h=h_sep, txt='5', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='LIMPIAR EL TECLADO Y MOUSE', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt=' ', border=1,ln=1,
                align='C', fill=0)
    #6
    pdf.cell(w=15, h=h_sep, txt='6', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='LIMPIAR LA IMPRESORA', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt=' ', border=1,ln=1,
                align='C', fill=0)
    #7
    pdf.cell(w=15, h=h_sep, txt='7', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='OTROS', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt=' ', border=1,ln=1,
                align='C', fill=0)  

    pdf.multi_cell(w=0, h=h_sep, txt='MANTENIMIENTO DE SOFTWARE', border=1,
                align='C', fill=0)
    
    #1
    pdf.cell(w=15, h=h_sep, txt='1', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='RESPALDAR LOS DRIVERS', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt='', border=1,ln=1,
                align='C', fill=0)
    #2
    pdf.cell(w=15, h=h_sep, txt='2', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='CHECKDISK', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt=' ', border=1,ln=1,
                align='C', fill=0)
    #3
    pdf.cell(w=15, h=h_sep, txt='3', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='CREAR PUNTO DE RESTAURACION INICIAL', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt='', border=1,ln=1,
                align='C', fill=0)
    #4
    pdf.cell(w=15, h=h_sep, txt='4', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='DESCARGAR ACTUALIZACIONES DE WINDOWS', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt='', border=1,ln=1,
                align='C', fill=0)
    #5
    pdf.cell(w=15, h=h_sep, txt='5', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='ACTUALIZAR EL ANTIVIRUS', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt=' ', border=1,ln=1,
                align='C', fill=0)
    #6
    pdf.cell(w=15, h=h_sep, txt='6', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='ELIMINAR ARCHIVOS TEMPORALES', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt=' ', border=1,ln=1,
                align='C', fill=0)
    #7
    pdf.cell(w=15, h=h_sep, txt='7', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='ANALIZAR EL SISTEMA CONTRA MALWARE', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt=' ', border=1,ln=1,
                align='C', fill=0)
    #8
    pdf.cell(w=15, h=h_sep, txt='8', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='DEPURAR EL REGISTRO', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt=' ', border=1,ln=1,
                align='C', fill=0)
    #9
    pdf.cell(w=15, h=h_sep, txt='9', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='CREAR UN PUNTO DE RESTAURACION INICIAL', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt=' ', border=1,ln=1,
                align='C', fill=0)
    #10
    pdf.cell(w=15, h=h_sep, txt='10', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='DESFRAGMENTAR DISCO DURO', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt=' ', border=1,ln=1,
                align='C', fill=0)
    #11
    pdf.cell(w=15, h=h_sep, txt='11', border=1,
                align='C', fill=0)
    pdf.cell(w=88, h=h_sep, txt='OTROS', border=1,
                align='L', fill=0)
    pdf.cell(w=87, h=h_sep, txt=' ', border=1,ln=1,
                align='C', fill=0)
    
    pdf.cell(w=95, h=h_sep, txt='FIRMA RESPONSABLE DEL SERVICIO', border=1,
                align='C', fill=0)
    pdf.cell(w=95, h=h_sep, txt='FIRMA Y SELLO ENCARGADO DE RECEPCION', border=1,ln=1,
                align='C', fill=0)
    pdf.cell(w=95, h=20, txt='', border=1,
                align='C', fill=0)
    pdf.cell(w=95, h=20, txt='', border=1,ln=1,
                align='C', fill=0)


    # Devolver el PDF como una respuesta HTTP
    response = HttpResponse(pdf.output(dest='S').encode('latin1'), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte.pdf"'

    return response

