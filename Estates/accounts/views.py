from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import UserSerializer , LogoutSerializer
from rest_framework.views import APIView
from rest_framework import permissions, status
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):                       # WORKS
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            data = request.data

            name = data['name']
            email = data['email']
            email = email.lower()
            password = data['password']
            re_password = data['re_password']



            if password == re_password:
                if len(password) >= 8:
                    if not User.objects.filter(email=email).exists():

                            user = User.objects.create_user(name=name, email=email, password=password)
                            refresh = RefreshToken.for_user(user)
                            access_token = str(refresh.access_token)


                            return Response(
                                {
                                'success': 'User created successfully',
                                'name': user.name,
                                'refresh': str(refresh),
                                'access': access_token,

                                 },
                                status=status.HTTP_201_CREATED
                            )

                    else:
                        return Response(
                            {'error': 'User with this email already exists'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                        {'error': 'Password must be at least 8 characters in length'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'error': 'Passwords do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong when registering an account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class RetrieveUserView(APIView):                       # WORKS
    permission_classes = (IsAuthenticated)

    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving user details'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class LogoutAPIView(generics.GenericAPIView):           # WORKS
     serializer_class = LogoutSerializer
     permission_classes = (permissions.IsAuthenticated,)
     def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {'success': 'Logged out successfully'},
                status=status.HTTP_200_OK
            )
        except:
              return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


