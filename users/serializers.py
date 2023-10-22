from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'repeat_password']

    def validate(self, attrs):
        repeat_password = attrs.pop('repeat_password')
        if attrs['password'] != repeat_password:
            raise serializers.ValidationError("Пароли не совпадают")

        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует")

        return attrs
