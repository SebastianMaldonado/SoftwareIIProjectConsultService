from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, LogSerializer
from .models import UserProfile, Log
# Create your views here.

from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import IsOwnUser

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters
from django_filters import rest_framework as django_filters
from django_filters.rest_framework import DjangoFilterBackend

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class LogFilter(django_filters.FilterSet):
    user_doc = django_filters.NumberFilter(field_name='user_doc', lookup_expr='exact')
    action = django_filters.CharFilter(field_name='action', lookup_expr='exact')

    class Meta:
        model = Log
        fields = ['user_doc', 'action']

class LogViewSet(ModelViewSet):
    serializer_class = LogSerializer
    queryset = Log.objects.all()
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = LogFilter
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('user_doc', openapi.IN_QUERY, description="Filter by user_doc", type=openapi.TYPE_STRING),
            openapi.Parameter('action', openapi.IN_QUERY, description="Filter by action", type=openapi.TYPE_STRING),
        ]
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Perform any additional logic here if needed
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()
    lookup_field = 'doc_num'
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        Log.objects.create(action="DELETE", user_doc=instance.doc_num, user_profile=instance)

        user = instance.user
        instance.delete()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)