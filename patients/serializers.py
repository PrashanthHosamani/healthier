from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
        read_only_fields = ("created_by", "created_at", "updated_at",)
        
        def validate_age(self, value):
            if value < 0:
                raise serializers.ValidationError("Age must be greater then 0")
    
            if value > 120:
                raise serializers.ValidationError("Age can not exceed 120")
            
            return value
        
        def validate_phone(self, value):
            cleaned_phone = value.stripe()
            
            if not cleaned_phone.is_digit():
                raise serializers.ValidationError("Phone number must contain only digits")
            
            if len(value) < 10:
                raise serializers.ValidationError("Phone number is invalid")
            
            return cleaned_phone