from django.urls import include, path

from .views import *
from rest_framework.routers import DefaultRouter

from .views.students import StudentsViewSet

app_name = "student_portal"
router = DefaultRouter()
router.register(r"students", StudentsViewSet, basename="students")
urlpatterns = [
    path("", include(router.urls)),
    # path("students/", StudentsViewSet.as_view(), name="students"),
]