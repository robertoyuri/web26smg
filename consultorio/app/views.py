from gc import get_objects

from django.shortcuts import render, redirect
from.models import Paciente


# Create your views here.

def home(request):
    return render(request, 'home.html')

def paciente_form(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        convenio = request.POST['convenio']
        telefone = request.POST['telefone']
        email = request.POST['email']
        nascimento = request.POST['nascimento']

        p = Paciente.objects.create(nome=nome, cpf=cpf, convenio=convenio,
                     telefone=telefone, email=email,
                     nascimento=nascimento)
        print(p.id)

        return redirect('app:paciente_list')

    return render(request, 'paciente_form.html')

def paciente_list(request):
    pacientes = Paciente.objects.all()
    #get_objects(Paciente)
    return render(request, 'paciente_list.html',
                  {'pacientes': pacientes})

def paciente_edit(request, pk):
    if pk:
        paciente = Paciente.objects.get(pk=pk)
    else:
        paciente = None

    if request.method == 'POST':
        paciente.nome = request.POST['nome']
        paciente.cpf = request.POST['cpf']
        paciente.convenio = request.POST['convenio']
        paciente.telefone = request.POST['telefone']
        paciente.email = request.POST['email']
        paciente.nascimento = request.POST['nascimento']
        paciente.save()
        print(paciente.id)

        return redirect('app:paciente_list')
    return render(request, 'paciente_form.html', {'paciente': paciente})

def paciente_delete(request, pk):
    if pk:
        paciente = Paciente.objects.get(pk=pk)
        paciente.delete()
        return redirect('app:paciente_list')