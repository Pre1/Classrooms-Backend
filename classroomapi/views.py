from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from .serializers import ClassroomListSerializer, ClassroomDetailSerializer, ClassroomCreateUpdateSerializer, UserRegisterSerializer, UserLoginSerializer
from .models import Classroom
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsTeacher


class ClassroomListAPIView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer

class ClassroomDetailAPIView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassroomCreateAPIView(CreateAPIView):
    serializer_class = ClassroomCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class ClassroomUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
    permission_classes = [IsAuthenticated, IsTeacher]

class ClassroomDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
    permission_classes = [IsAuthenticated, IsTeacher]


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