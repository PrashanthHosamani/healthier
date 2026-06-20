from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at",)

    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError(
                "Doctor name must contain at least 2 characters."
            )
        return value

    def validate_specialization(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError(
                "Specialization is required."
            )
        return value

    def validate_phone(self, value):
        cleaned_phone = value.strip()

        if not cleaned_phone.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits."
            )

        if len(cleaned_phone) != 10:
            raise serializers.ValidationError(
                "Phone number must be exactly 10 digits."
            )

        return cleaned_phone