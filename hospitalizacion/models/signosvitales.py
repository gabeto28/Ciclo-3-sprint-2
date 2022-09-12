from tkinter import CASCADE
from django.db import models
from .paciente import paciente
from .medico import medico
from .enfermero import enfermero
from .familiar import familiar

class signosvitales(models.Model):

    id_signosvitales= models.IntegerField(primary_key=True)
    signosvitales= models.CharField(max_length=200)
    fecha= models.DateField()
    medico_fk=models.ForeignKey(medico,on_delete=models.CASCADE)
    enfermero_fk=models.ForeignKey(enfermero,on_delete=models.CASCADE)
    familiar_fk=models.ForeignKey(familiar,on_delete=models.CASCADE)
    paciente_fk=models.ForeignKey(paciente,on_delete=models.CASCADE)
