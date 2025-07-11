from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = []
    parser_classes = [MultiPartParser, FormParser]

    queryset = User.objects.all()
    serializer_class = UserSerializer


# class SkillsViewSet(viewsets.ModelViewSet):
#     queryset = Skills.objects.all()
#     serializer_class = SkillsSerializer
