
from django.contrib import admin
from django.urls import path, include
from school.views import RegistrationViewSet, StudentViewSet, CourseViewSet, ListaRegistrationStudent, ListSudentRegistered
from rest_framework import routers

router = routers.DefaultRouter()
router.register('student', StudentViewSet, basename='Student')
router.register('course', CourseViewSet, basename='Course')
router.register('registration', RegistrationViewSet,basename='Registration')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('student/<int:pk>/registration/', ListaRegistrationStudent.as_view()),
    path('course/<int:pk>/registration/',ListSudentRegistered.as_view()),
]
