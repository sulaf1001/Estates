from django.urls import path
from .views import RegisterView, RetrieveUserView , LogoutAPIView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('me/', RetrieveUserView.as_view()),
    path('logout/', LogoutAPIView.as_view()),


]