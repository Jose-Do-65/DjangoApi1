from django.db import models

# Create your models here.
class generos (models.Model):
    generos_id = models.AutoField(primary_key=True)
    tipo_genero = models.CharField(max_length=255)
    
    class Meta:
        db_table = "generos"
        
class usuarios (models.Model):
    usuarios_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    fk_genero = models.ForeignKey(generos, on_delete=models.CASCADE, default=0)
    
    class Meta:
        db_table = "usuarios"