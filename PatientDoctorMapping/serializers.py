from rest_framework import serializers
from .models import PatientDoctorMapping


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(
        source="patient.name",
        read_only=True )

    doctor_name = serializers.CharField(
        source="doctor.name",
        read_only=True )
    

    class Meta:
        model = PatientDoctorMapping
        fields = "id", "patient", "patient_name", "doctor", "doctor_name", "assigned_by", "assigned_at"
        read_only_fields = ( "assigned_by", "assigned_at",)
        

    def validate(self, attrs):
        patient = attrs.get("patient")
        doctor = attrs.get("doctor")

        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError(
                "This doctor is already assigned to the patient."
            )
        return attrs