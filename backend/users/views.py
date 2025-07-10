
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class SkillsViewSet(viewsets.ModelViewSet):
#     queryset = Skills.objects.all()
#     serializer_class = SkillsSerializer
