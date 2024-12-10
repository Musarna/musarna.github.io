from rest_framework import serializers
from pruebaApp.models import Juguete

class JugueteSerializar(serializers.ModelSerializer):
    class Meta:
        model  = Juguete
        fields = '__all__'