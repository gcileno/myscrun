from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Rota para login (recebe username/password e devolve o token)
    path('authorize/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Rota para renovar o token expirado
    path('authorize/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]