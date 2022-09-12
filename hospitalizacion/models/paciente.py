from tkinter import CASCADE
from django.db import models
from .usuario import usuario
from .medico import medico
from .enfermero import enfermero
from .familiar import familiar

class paciente(models.Model):

    id_paciente= models.IntegerField(primary_key=True)
    nombresapellidos= models.CharField(max_length=100)
    telefono=models.IntegerField()
    emali=models.CharField(max_length=50)
    medico_fk=models.ForeignKey(medico,on_delete=models.CASCADE)
    enfermero_fk=models.ForeignKey(enfermero,on_delete=models.CASCADE)
    familiar_fk=models.ForeignKey(familiar,on_delete=models.CASCADE)
    usuario_fk= models.ForeignKey(usuario,on_delete=models.CASCADE)