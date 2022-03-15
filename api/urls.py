from django.urls import path
from . import views
from .api import views as test

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', test.test_end_point, name='test'),
    path('', views.get_routes),
]
