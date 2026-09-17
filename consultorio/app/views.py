from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def paciente_form(request):
    return render(request, 'paciente_form.html')

def paciente_list(request):
    return render(request, 'paciente_list.html')