from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
     
    # def get_len_name(self, object):
    #     return len(object.name)
    
    # def validate_name(self, value): # field level validation
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value
    
    # def validate(self, data): # object-level validation
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Name and description should be different')
    #     return data

class StreamPlatformSerializer(serializers.ModelSerializer):
    # Serializers Relations (RelatedKeyField)
    watchlist = WatchListSerializer(many=True, read_only=True) # nested serializers

    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # Provides link for every object
    # watchlist = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='individual-movie')
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is very short')

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data['name']
#         instance.description = validated_data['description']
#         instance.active = validated_data['active']
#         instance.save()
#         return instance

    # def validate_name(self, value): # field level validation
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value
    
    # def validate(self, data): # object-level validation
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Name and description should be different')
    #     return data
