from rest_framework import serializers
from .models import *

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model=dataset
        fields='__all__'
