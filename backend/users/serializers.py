from rest_framework import serializers
from .models import User, Skills


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        exclude = ['user']


class UserSerializer(serializers.ModelSerializer):
    skills = SkillsSerializer()

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id', 'groups', 'user_permissions',
                            'is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        skills_data = validated_data.pop('skills', {})
        user = User.objects.create(**validated_data)
        if skills_data:
            Skills.objects.create(user=user, **skills_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
