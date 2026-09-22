from django.urls import path
from .views import home, paciente_form, paciente_list, paciente_edit, paciente_delete
from .views import medico_form, medico_list, medico_edit, medico_delete

app_name = "app"

urlpatterns = [
    path('', home, name='home'),
    path('paciente/', paciente_list, name='paciente_list'),
    path('paciente/cadastrar/', paciente_form, name='paciente_form'),
    path('paciente/editar/<int:pk>', paciente_edit, name='paciente_edit'),
    path('paciente/deletar/<int:pk>', paciente_delete, name='paciente_delete'),
    path('medico/cadastrar/', medico_form, name='medico_form'),
    path('medico/', medico_list, name='medico_list'),
    path('medico/editar/<int:pk>', medico_edit, name='medico_edit'),
    path('medico/deletar/<int:pk>', medico_delete, name='medico_delete'),
]
