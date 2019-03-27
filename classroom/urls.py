from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classroomapi import views
from classroomapi.views import ClassroomListAPIView, ClassroomDetailAPIView, ClassroomCreateAPIView, ClassroomUpdateView, ClassroomDeleteView
from classroomapi.views import StudentCreateAPIView, StudentUpdateAPIView, StudentDeleteAPIView
from classroomapi.views import UserRegisterView, UserLoginView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/classrooms/list/', ClassroomListAPIView.as_view(), name='classroom-list'),
    path('api/classrooms/detail/<int:classroom_id>/', ClassroomDetailAPIView.as_view(), name='classroom-detail'),
    path('api/classrooms/create/', ClassroomCreateAPIView.as_view(), name='classroom-create'),
    path('api/classrooms/update/<int:classroom_id>/', ClassroomUpdateView.as_view(), name='classroom-update'),
    path('api/classrooms/delete/<int:classroom_id>/', ClassroomDeleteView.as_view(), name='classroom-delete'),

    path('api/students/create/', StudentCreateAPIView.as_view(), name='student-create'),
    path('api/students/update/<int:student_id>/', StudentUpdateAPIView.as_view(), name='student-update'),
    path('api/students/delete/<int:student_id>/', StudentDeleteAPIView.as_view(), name='student-delete'),

    path('api/user/register/', UserRegisterView.as_view(), name='user-register'),
    path('api/user/login/', obtain_jwt_token, name='user-login'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)