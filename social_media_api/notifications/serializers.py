from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source="actor.username", read_only=True)

    class Meta:
        model = Notification
        fields = ["id", "recipient", "actor_username", "verb", "target_object_id", "created_at", "read"]
