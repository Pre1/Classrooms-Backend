from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classroomapi import views
from classroomapi.views import ClassroomListAPIView, ClassroomDetailAPIView, ClassroomCreateAPIView, ClassroomUpdateView, ClassroomDeleteView
from classroomapi.views import UserRegisterView, UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/classrooms/list/', ClassroomListAPIView.as_view(), name='api-classroom-list'),
    path('api/classrooms/detail/<int:classroom_id>/', ClassroomDetailAPIView.as_view(), name='api-classroom-detail'),
    path('api/classrooms/create/', ClassroomCreateAPIView.as_view(), name='api-classroom-create'),
    path('api/classrooms/update/<int:classroom_id>/', ClassroomUpdateView.as_view(), name='api-classroom-update'),
    path('api/classrooms/delete/<int:classroom_id>/', ClassroomDeleteView.as_view(), name='api-classroom-delete'),

    path('api/user/register/', UserRegisterView.as_view(), name='api-user-register'),
    path('api/user/login/', UserLoginView.as_view(), name='api-user-login'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)