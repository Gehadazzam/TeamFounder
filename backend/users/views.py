from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['job', 'skills__python', 'skills__javascript', 'skills__react', 'skills__django', 'skills__flask',
                        'skills__sql', 'skills__no_sql', 'skills__java', 'skills__c', 'skills__cpp', 'skills__csharp', 'skills__php', 'skills__ruby']

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        elif self.action == 'destroy':
            return [IsAdminUser()]
        return super().get_permissions()


# class SkillsViewSet(viewsets.ModelViewSet):
#     queryset = Skills.objects.all()
#     serializer_class = SkillsSerializer
