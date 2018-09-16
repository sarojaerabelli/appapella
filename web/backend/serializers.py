from rest_framework import serializers
from backend.models import Recorder

class RecorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recorder
        fields = '__all__'