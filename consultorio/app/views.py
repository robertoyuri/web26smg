from django.shortcuts import render, redirect, get_object_or_404
from.models import Paciente, Medico
from .forms import MedicoForm
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

def medico_form(request):
    form = MedicoForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('app:medico_list')
    return render(request, 'medico_form.html', {'form': form})

def medico_list(request):
    medicos = Medico.objects.all()
    return render(request, 'medico_list.html',
                  {'medicos': medicos})

def medico_edit(request, pk):
    medico = None
    if pk:
        medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = MedicoForm(request.POST, request.FILES, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('app:medico_list')
    else:
        form = MedicoForm(instance=medico)

    return render(request, 'medico_form.html', {'form': form})

def medico_delete(request, pk):
    if pk:
        medico = get_object_or_404(Medico, pk=pk)
        medico.delete()
        return redirect('app:medico_list')
    return render(request, 'medico_form.html')