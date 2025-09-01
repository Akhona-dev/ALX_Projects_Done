from rest_framework import serializers
from .models import Tasks
from django.contrib.auth.models import User

"""task serialiser"""

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

#-----------------------------------------
#user reg
#-----------------------------------------

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        # create user with hashed password
        user = User.objects.create_user(**validated_data)
        return user