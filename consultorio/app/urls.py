from django.urls import path
from .views import home, paciente_form, paciente_list

app_name = "app"

urlpatterns = [
    path('', home, name='home'),
    path('paciente/', paciente_list, name='paciente_list'),
    path('paciente/cadastrar/', paciente_form, name='paciente_form'),
]
