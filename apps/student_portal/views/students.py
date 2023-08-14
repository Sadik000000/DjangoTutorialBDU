from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework_extensions.mixins import DetailSerializerMixin

from apps.student_portal.models import Student
from apps.student_portal.serializers.students import StudentSerializer, GetStudentSerializer, PostStudentSerializer, \
    PutStudentSerializer, PatchStudentSerializer, ListStudentSerializer
from utils.mixin import StandardResultsSetPagination


class StudentsViewSet(DetailSerializerMixin, viewsets.ModelViewSet):
    queryset = Student.objects.all()
    max_paginate_by = 100
    serializer_class = StudentSerializer
    pagination_class = StandardResultsSetPagination
    # permission_classes = (IsAuthenticated,)
    #
    # def get_queryset(self):
    #     return Student.objects
    # @extend_schema(
    #     request=StudentSerializer,
    #     responses={201: StudentSerializer,
    #                200: StudentSerializer},
    # )
    def create(self, request):
        # your non-standard behaviour
        return super().create(request)

    def get_serializer_class(self):
        if self.action == 'list':
            return ListStudentSerializer
        elif self.action == 'retrieve':
            return GetStudentSerializer
        elif self.action == 'create':
            return PostStudentSerializer
        elif self.action == 'update':
            return PutStudentSerializer
        elif self.action == 'partial_update':
            return PatchStudentSerializer
        # elif self.action == 'destroy':
        #     return StudentSerializer
        else:
            return StudentSerializer


#
# `    def create(self, request):
#         # your non-standard behaviour
#         return super().create(request)