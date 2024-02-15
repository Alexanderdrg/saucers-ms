from rest_framework import serializers

from saucers.models import Saucer


class SaucerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saucer
        fields = '__all__'
