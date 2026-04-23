from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.db import transaction
from rest_framework_simplejwt.tokens import RefreshToken
from members.serializers.user import RegisterSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            'token': str(refresh.access_token),
            'member': {
                'id': user.member.id,
                'name': user.member.name,
            }
        }, status=status.HTTP_201_CREATED)