from django.urls import path
from django.urls import path, include

from .views import (
    UserProfileViewSet,
    LogViewSet,
)
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'logs', LogViewSet, basename="Log")

urlpatterns = [
    path('', include(router.urls)),
]

