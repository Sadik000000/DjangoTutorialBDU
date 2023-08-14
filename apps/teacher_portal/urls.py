from django.urls import include, path

from .views import *
from rest_framework.routers import DefaultRouter



app_name = "teacher_portal"
router = DefaultRouter()
# router.register(r"", , basename="")
urlpatterns = [
    path("", include(router.urls)),
    # path("students/", StudentsViewSet.as_view(), name="students"),
]