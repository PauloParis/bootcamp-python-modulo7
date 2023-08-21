from django.shortcuts import render, get_object_or_404, redirect
from laboratorio.models import *
from laboratorio.forms import LaboratorioForm

# Create your views here.


def agregar(request):
    if request.method == 'POST':
        formLaboratorio = LaboratorioForm(request.POST)
        if formLaboratorio.is_valid():
            formLaboratorio.save()
            return redirect('informacion')
    else:
        formLaboratorio = LaboratorioForm()
    return render(request, 'add.html', {'formLaboratorio': formLaboratorio})

contador = 0

def informacion(request):
    laboratorios = Laboratorio.objects.order_by('id')
    global contador
    contador += 1
    return render (request, 'info.html', {
        'Laboratorios': laboratorios,
        'contador': contador
        })

def actualizar(request, id):
    laboratorio = get_object_or_404(Laboratorio, pk=id)
    if request.method == 'POST':
        formLaboratorio = LaboratorioForm(request.POST, instance=laboratorio)
        if formLaboratorio.is_valid():
            formLaboratorio.save()
            return redirect('informacion')
    else:
        formLaboratorio = LaboratorioForm(instance=laboratorio)
    return render(request, 'edit.html', {'formLaboratorio': formLaboratorio})


def eliminar(request, id):
    laboratorio = get_object_or_404(Laboratorio, pk=id)
    return render(request, 'remove.html', {'laboratorio': laboratorio})

def eliminar_confirmar(request, id):
    laboratorio = get_object_or_404(Laboratorio, pk=id)
    if laboratorio:
        laboratorio.delete()
    return redirect('informacion')

