from django.db import models
from django.conf import settings

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey( "patients.Patient", on_delete=models.CASCADE, related_name="doctor_mappings")
    doctor = models.ForeignKey("doctors.Doctor", on_delete=models.CASCADE, related_name="patient_mappings")
    assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            "patient",
            "doctor"
        )

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"