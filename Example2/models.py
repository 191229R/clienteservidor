from django.db import models

# Create your models here.

class Example2(models.Model):
    name = models.CharField(max_length = 255, null = False)   #tipo de modelo
    #Retorna el valor que le va acontener que es name
    def __str__(self):
        return self.name 
    #asigna el nombre de la tabla
    class Meta:
        db_table = 'Example2'