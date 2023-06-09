from rest_framework import serializers
from .models import *

class GoogleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Google
        fields='__all__'

class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Meta
        fields='__all__'

class MicrosoftSerializer(serializers.ModelSerializer):
    class Meta:
        model=Microsoft
        fields='__all__'

class AppleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Apple
        fields='__all__'