from django.db import models

class usuario(models.Model):

    id_usuario= models.IntegerField(primary_key=True)
    contraseniausuarios= models.CharField(max_length=15)
    tipousuario= models.CharField(max_length=15)
    cedula=models.IntegerField()