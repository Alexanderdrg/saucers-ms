from rest_framework import serializers

from saucers.models import Saucer, Additional, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            'name'
        ]


class AdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additional
        fields = [
            'name'
        ]


class SaucerSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    additional = AdditionalSerializer(many=True)

    class Meta:
        model = Saucer
        fields = '__all__'
