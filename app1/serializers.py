from rest_framework import serializers 
from .models import app1modal1

class app1modal1Serializer(serializers.ModelSerializer): 
    class Meta: 
        model = app1modal1 
        fields = '__all__' 
