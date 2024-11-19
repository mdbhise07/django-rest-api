from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    assigned_users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all()
    )

    class Meta:
        model = Project
        fields = '__all__'