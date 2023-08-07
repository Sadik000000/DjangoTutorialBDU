from django.db import models

from utils.mixin import BaseModelMixin


# Create your models here.

class Student(BaseModelMixin):
    '''
        Student Database Schema
    '''
    first_name = models.CharField(name="first_name", max_length=256, null=True, blank=True)
    last_name = models.CharField(name="last_name", max_length=256, null=True, blank=True)
    email = models.EmailField(name="email", max_length=256)
    phone_number = models.CharField(name="phone_number", max_length=256, null=True, blank=True)
    address = models.CharField(name="address", max_length=256, null=True, blank=True)
    district = models.CharField(name="district", max_length=256, null=True, blank=True)
    division = models.CharField(name="division", max_length=256, null=True, blank=True)
    post_code = models.CharField(name="post_code", max_length=256, null=True, blank=True)
    rdf_number = models.CharField(name="rdf_number", max_length=256)
    dob = models.DateField(name="dob")
    current_year = models.CharField(name="current_year", max_length=256, null=True, blank=True)
    session = models.CharField(name="session", max_length=256, null=True, blank=True)
    roll_number = models.CharField(name="roll_number", max_length=256, null=True, blank=True)
    registration_number = models.CharField(name="registration_number", max_length=256, null=True, blank=True)
    is_active = models.BooleanField(name="is_active", default=True)

    def __str__(self):
        return "ID: " + str(self.id) + ", NAME: " + self.first_name + " " + self.last_name + ", EMAIL: " + self.email


class Teacher(BaseModelMixin):
    """
    Teacher Database Schema
    """
    first_name = models.CharField(name="first_name", max_length=256, null=True, blank=True)
    last_name = models.CharField(name="last_name", max_length=256, null=True, blank=True)
    email = models.EmailField(name="email", max_length=256)
    phone_number = models.CharField(name="phone_number", max_length=256, null=True, blank=True)
    address = models.CharField(name="address", max_length=256, null=True, blank=True)
    district = models.CharField(name="district", max_length=256, null=True, blank=True)
    division = models.CharField(name="division", max_length=256, null=True, blank=True)
    post_code = models.CharField(name="post_code", max_length=256, null=True, blank=True)
    rdf_number = models.CharField(name="rdf_number", max_length=256)
    dob = models.DateField(name="dob")
    position = models.CharField(name="position", max_length=256)
    is_active = models.BooleanField(name="is_active", default=True)
    joining_date = models.DateField(name="joining_date")

    def __str__(self):
        return "ID: " + str(self.id) + ", NAME: " + self.first_name + " " + self.last_name + ", EMAIL: " + self.email


class Subject(BaseModelMixin):
    """
    Subject Database Schema
    """
    name = models.CharField(name="name", max_length=256)
    code = models.CharField(name="code", max_length=256)
    is_active = models.BooleanField(name="is_active", default=True)

    def __str__(self):
        return "ID: " + str(self.id) + ", NAME: " + self.name + ", CODE: " + self.code


class StudentSubjectAssociation(BaseModelMixin):
    """
    Student Subject Database Schema
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    is_active = models.BooleanField(name="is_active", default=True)

    def __str__(self):
        return "ID: " + str(self.id) + ", STUDENT: " + str(self.student) + ", SUBJECT: " + str(self.subject)


class TeacherSubjectAssociation(BaseModelMixin):
    """
    Teacher Subject Database Schema
    """
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    is_active = models.BooleanField(name="is_active", default=True)

    def __str__(self):
        return "ID: " + str(self.id) + ", TEACHER: " + str(self.teacher) + ", SUBJECT: " + str(self.subject)
