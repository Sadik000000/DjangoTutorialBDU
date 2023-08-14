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

class GetStudentSerializer(serializers.ModelSerializer):
    """
    Student Serializer
    """
    class Meta:
        model = Student
        exclude = ('created_at', 'updated_at', 'is_active')

class PostStudentSerializer(GetStudentSerializer):
    pass

class PutStudentSerializer(GetStudentSerializer):
    pass

class PatchStudentSerializer(GetStudentSerializer):
    pass

class ListStudentSerializer(GetStudentSerializer):
    class Meta:
        model = Student
        fields=('id', 'email', 'first_name', 'last_name')