from rest_framework import viewsets, generics
from school.models import Student, Course, Registration
from school.serializer import ListRegistrationStudentSerializer, StudentSerializer, CourseSerializer, RegistrationSerializer, ListStudentRegisteredSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentViewSet(viewsets.ModelViewSet):
    """Showing all male and female students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    """Showing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RegistrationViewSet(viewsets.ModelViewSet):
    """Showing all registry"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaRegistrationStudent(generics.ListAPIView):
    """Registering a student's enrollment"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])   
        return queryset
    serializers_class = ListRegistrationStudentSerializer 
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListSudentRegistered(generics.ListAPIView):
    """Listing Students Enrolled in a Course"""
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentRegisteredSerializer  
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]