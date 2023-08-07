from rest_framework import serializers

from apps.student_portal.models import Student


class StudentSerializer(serializers.ModelSerializer):
    """
    Student Serializer
    """
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ('id', 'created_at', 'updated_at', 'user')
