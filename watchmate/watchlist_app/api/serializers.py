from rest_framework import serializers
from watchlist_app.models import Movie

def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError('Name is very short')

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.active = validated_data['active']
        instance.save()
        return instance

    # def validate_name(self, value): # field level validation
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value
    
    # def validate(self, data): # object-level validation
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Name and description should be different')
    #     return data
