from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .serializers import ClassroomDetailSerializer, ClassroomListCreateUpdateSerializer, UserRegisterSerializer, UserLoginSerializer
from .serializers import StudentCreateUpdateSerializer, StudentDetailSerializer

from .models import Classroom, Student
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsTeacher


class ClassroomListAPIView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListCreateUpdateSerializer

class ClassroomDetailAPIView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomCreateAPIView(CreateAPIView):
	serializer_class = ClassroomListCreateUpdateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)

class ClassroomUpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'
	permission_classes = [IsAuthenticated, IsTeacher]

class ClassroomDeleteView(DestroyAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'
	permission_classes = [IsAuthenticated, IsTeacher]

class StudentCreateAPIView(CreateAPIView):
	serializer_class = StudentCreateUpdateSerializer
	permission_classes = [IsAuthenticated, IsTeacher]
	def post(self, request):
		my_data = request.data
		serializer = self.serializer_class(data=my_data)
		if serializer.is_valid():
			valid_data = serializer.data
			new_data = {
				'first_name': valid_data['first_name'],
				'last_name': valid_data['last_name'],
				'dob': valid_data['dob'],
				'exam_grade': valid_data['exam_grade'],
				'classroom': Classroom.objects.get(id=valid_data['classroom']),
				'gender': valid_data['gender']
			}
			student=Student.objects.create(**new_data)
			return Response(StudentDetailSerializer(student).data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class StudentUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'student_id'
	permission_classes = [IsAuthenticated]

class StudentDeleteAPIView(DestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'student_id'
	permission_classes = [IsAuthenticated]

class UserRegisterView(CreateAPIView):
	serializer_class = UserRegisterSerializer

class UserLoginView(APIView):
	serializer_class = UserLoginSerializer

	def post(self, request):
		my_data = request.data
		serializer = UserLoginSerializer(data=my_data)
		if serializer.is_valid(raise_exception=True):
			valid_data = serializer.data
			return Response(valid_data, status=HTTP_200_OK)
		return Response(serializer.errors, HTTP_400_BAD_REQUEST)