from rest_framework import serializers
from .models import User, Skills


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    skills = SkillsSerializer()

    class Meta:
        model = User
        fields = '__all__'
