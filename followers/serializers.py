from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower
from profiles.serializers import ProfileSerializer

class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model
    Create method handles the unique constraint on 'owner' and 'followed'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed = ProfileSerializer(read_only=True)
    class Meta:
        model = Follower
        fields = ['id', 'owner', 'created_at', 'followed']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})