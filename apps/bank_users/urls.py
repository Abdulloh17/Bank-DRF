from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from .views import UserApiViewSet

router = DefaultRouter()
router.register('users', UserApiViewSet, basename='users')

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='api_login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls