from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email' )

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    # Define error messages
    error_messages = {
        'bad_token': 'Token is invalid or has already been blacklisted.'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')