from django.urls import path
from .views import (UserListViews, UserCreatViews)

app_name = 'api-v2'


urlpatterns = [
    path('UserList/', UserListViews.as_view(), name='user_list'),
    path('CreatUser/<int:pk>', UserCreatViews.as_view(), name='register'),
    ]