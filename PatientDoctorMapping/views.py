from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

class PatientDoctorMappingViewSet(ModelViewSet):

    serializer_class = (PatientDoctorMappingSerializer)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = (PatientDoctorMapping.objects.select_related("patient", "doctor", "assigned_by"))

        patient_id = self.request.query_params.get("patient")

        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            assigned_by=self.request.user
        )