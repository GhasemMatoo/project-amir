from django.urls import path
from rest_framework_simplejwt.views import (
    TokenVerifyView, TokenRefreshView,)
from .views import (
    UserListViews, UserCreatViews, UserUpdateViews, CustomTokenObtainPairView)

app_name = 'api-v1'


urlpatterns = [
    path('UserList/', UserListViews.as_view(), name='user_list'),
    path('CreatUser/', UserCreatViews.as_view(), name='register'),
    path('updateUser/<int:pk>', UserUpdateViews.as_view(), name='Edit_User'),
    # JWT
    path('jwt/token/create', CustomTokenObtainPairView.as_view(), name='create-token'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('jwt/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
