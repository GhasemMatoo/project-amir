from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.models import CustomUser
from .serializers import CustomUserSerializer, UserCreatSerializer, UserUpdateSerializer


class UserListViews(ListAPIView):
    """
        View in list user object HTTP Methods GET
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


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