from django.db import models
from .usuario import usuario

class auxiliarhospital(models.Model):

    id_auxiliar= models.IntegerField(primary_key=True)
    nombresapellidos= models.CharField(max_length=100)
    telefono= models.IntegerField()
    usuario_fk= models.ForeignKey(usuario,related_name='usuario auxiliar',on_delete=models.CASCADE)