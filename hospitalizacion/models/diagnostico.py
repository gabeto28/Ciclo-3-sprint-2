from tkinter import CASCADE
from django.db import models
from .medico import medico
from .paciente import paciente
from .enfermero import enfermero
from .familiar import familiar


class diagnostico(models.Model):

    id_diagnostico= models.IntegerField(primary_key=True)
    diagnostico= models.CharField(max_length=500)
    sugernecia= models.CharField(max_length=500)
    fecha= models.DateField()
    medico_fk=models.ForeignKey(medico,on_delete=models.CASCADE)
    enfermero_fk=models.ForeignKey(enfermero,on_delete=models.CASCADE)
    familiar_fk=models.ForeignKey(familiar,on_delete=models.CASCADE)
    paciente_fk=models.ForeignKey(paciente,on_delete=models.CASCADE)
