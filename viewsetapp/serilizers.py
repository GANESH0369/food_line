from rest_framework import serializers
from .models import employesviws,login

class seriempoly(serializers.ModelSerializer):
    class Meta:
        model=employesviws
        fields='__all__'
        
class serilogin(serializers.ModelSerializer):
    class Meta:
        model=login
        fields='__all__'