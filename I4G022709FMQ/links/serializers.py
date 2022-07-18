from rest_framework import serializers
from .models import Link


# Create your class here
class LinkSerializer(serializers.ModelSerializer):
    class meta:
        model = Link
        field = '__all__'