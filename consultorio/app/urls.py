from django.urls import path
from .views import home, paciente_form, paciente_list, paciente_edit, paciente_delete

app_name = "app"

urlpatterns = [
    path('', home, name='home'),
    path('paciente/', paciente_list, name='paciente_list'),
    path('paciente/cadastrar/', paciente_form, name='paciente_form'),
    path('paciente/editar/<int:pk>', paciente_edit, name='paciente_edit'),
    path('paciente/deletar/<int:pk>', paciente_delete, name='paciente_delete'),
]
