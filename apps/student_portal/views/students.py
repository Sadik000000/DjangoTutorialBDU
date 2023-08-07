from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.student_portal.models import Student
from apps.student_portal.serializers.students import StudentSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = (IsAuthenticated,)
    #
    # def get_queryset(self):
    #     return Student.objects
    @extend_schema(
        request=StudentSerializer,
        responses={201: StudentSerializer,
                   200: StudentSerializer},
    )
    def create(self, request):
        # your non-standard behaviour
        return super().create(request)


#
# `    def create(self, request):
#         # your non-standard behaviour
#         return super().create(request)