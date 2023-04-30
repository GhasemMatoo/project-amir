from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'created_date', 'update_date', 'user_created_date',
                  'user_update_date', 'username'
        ]
     
        
class UserCreatSerializer(serializers.ModelSerializer):
    Re_password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'username', 'password', 'Re_password', 'created_date',
                  'update_date', 'user_created_date', 'user_update_date'
        ]

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('Re_password'):
            raise serializers.ValidationError({'detail': 'Password doesnt match'})
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('Re_password')
        return CustomUser.objects.create(**validated_data)