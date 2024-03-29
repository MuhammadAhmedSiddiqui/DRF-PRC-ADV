from rest_framework import serializers

from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        return self.model.objects.create_user(**validated_data)
