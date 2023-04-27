from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class SignInView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

