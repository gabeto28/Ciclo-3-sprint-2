from tkinter import CASCADE
from django.db import models
from .usuario import usuario

class familiar(models.Model):

    id_familiar= models.IntegerField(primary_key=True)
    nombresapellidos= models.CharField(max_length=100)
    telefono=models.IntegerField()
    emali=models.CharField(max_length=50)
    usuario_fk=models.ForeignKey(usuario,on_delete=models.CASCADE)