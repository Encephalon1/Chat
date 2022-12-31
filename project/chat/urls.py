from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'chats', GroupChatViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='profile'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('create/<int:pk>', LoadAvatar.as_view(), name='avatar_load'),
    path('img/<int:pk>', LoadAvatar.home, name='home'),
    path('upload/<int:pk>', LoadAvatar.file_upload)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
