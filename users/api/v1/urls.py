from django.urls import path
from .views import (UserListViews, UserCreatViews, UserUpdateViews)

app_name = 'api-v2'


urlpatterns = [
    path('UserList/', UserListViews.as_view(), name='user_list'),
    path('CreatUser/', UserCreatViews.as_view(), name='register'),
    path('updateUser/<int:pk>', UserUpdateViews.as_view(), name='Edit_User'),
    ]