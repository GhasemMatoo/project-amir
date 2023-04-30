from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.models import CustomUser
from .serializers import CustomUserSerializer


class UserListViews(ListAPIView):
    """
        View in list user object HTTP Methods GET
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserCreatViews(RetrieveUpdateAPIView):
    """
        View in list user object HTTP Methods GET
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "pk"