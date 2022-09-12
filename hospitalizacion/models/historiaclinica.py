from tkinter import CASCADE
from django.db import models
from .paciente import paciente
from .medico import medico
from .familiar import familiar
from.diagnostico import diagnostico

class historiaclinica(models.Model):

    id_historiaclinica= models.IntegerField(primary_key=True)
    resumen= models.CharField(max_length=500)
    diagnostico_fk=models.ForeignKey(diagnostico,on_delete=models.CASCADE)
    medico_fk=models.ForeignKey(medico,on_delete=models.CASCADE)
    familiar_fk=models.ForeignKey(familiar,on_delete=models.CASCADE)
    paciente_fk=models.ForeignKey(paciente,on_delete=models.CASCADE)