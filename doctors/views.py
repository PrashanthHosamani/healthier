from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(ModelViewSet):
    
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    queryset = Doctor.objects.all()
