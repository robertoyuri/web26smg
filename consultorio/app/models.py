from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    convenio = models.CharField(blank=True, null=True,max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank=True, null=True)
    nascimento = models.DateField()

    def __str__(self):
        return self.nome + ' - ' + self.cpf

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=10)
    uf_crm = models.CharField(max_length=2)
    especialidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome + ' - ' + self.crm

class Consulta(models.Model):
    data = models.DateTimeField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    prontuario = models.TextField(blank=True, null=True)
    consultorio = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.paciente.nome + ' - ' + self.medico.nome

