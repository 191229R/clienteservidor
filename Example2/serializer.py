from rest_framework import routers, serializers, viewsets
from Example2.models import Example2

class Example2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Example2
        fields = ('__all__')  #Sirve para filtrar el modelo que deseamos
        
    