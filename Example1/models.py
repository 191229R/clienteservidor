from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Example1(models.Model):
    name = models.CharField(max_length = 255, null = False)
    edad = models.IntegerField(validators=[MaxValueValidator(99), MinValueValidator(1)])
    direccion = models.CharField(max_length = 200)
    curp = models.CharField('volumen', max_length=16, validators=[MinLengthValidator(16)])
    #Retorna el valor que le va acontener que es name
    
    def __str__(self):
        return self.name,self.edad,self.direccion,self.curp 
    #asigna el nombre de la tabla
    class Meta:
        db_table = 'Example1'
    
    