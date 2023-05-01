from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import CustomUser
from .serializers import (CustomUserSerializer, UserCreatSerializer, UserUpdateSerializer,
                          CustomTokenObtainPairSerializer
                          )


class UserListViews(ListAPIView):
    """
        View in list user object HTTP Methods GET
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


class UserCreatViews(CreateAPIView):
    """
        creat user object HTTP Methods Post
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserCreatSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserUpdateViews(RetrieveUpdateAPIView):
    """
        Edit user object HTTP Methods POUT PATCH
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "pk"


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
