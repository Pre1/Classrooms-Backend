from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Classroom, Student
from rest_framework_jwt.settings import api_settings

class TecherSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username']

class StudentDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields=[
			'id',
			'first_name',
			'last_name',
			'dob',
			'exam_grade',
			'gender'
		]

class ClassroomDetailSerializer(serializers.ModelSerializer):
	students = StudentDetailSerializer(many=True)
	teacher = TecherSerializer()
	class Meta:
		model = Classroom
		fields = ['id', 'subject', 'grade', 'year', 'teacher', 'students']

class ClassroomListCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'subject', 'grade', 'year']

class StudentCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ['first_name', 'last_name', 'dob', 'exam_grade', 'classroom', 'gender']

class UserRegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	token = serializers.CharField(allow_blank=True, read_only=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'password', 'email', 'token']

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		new_user = User(username=username)
		new_user.set_password(password)
		new_user.save()

		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

		payload = jwt_payload_handler(new_user)
		token = jwt_encode_handler(payload)

		validated_data["token"] = token
		return validated_data

class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(write_only=True)
	token = serializers.CharField(allow_blank=True, read_only=True)

	def validate(self, data):
		my_username = data.get('username')
		my_password = data.get('password')
		try:
			user_obj = User.objects.get(username=my_username)
			print(user_obj)
			jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
			jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

			payload = jwt_payload_handler(user_obj)
			token = jwt_encode_handler(payload)

			data["token"] = token
		except:
			raise serializers.ValidationError("This username does not exist")

		if not user_obj.check_password(my_password):
			raise serializers.ValidationError("Incorrect username/password combination!")

		return data