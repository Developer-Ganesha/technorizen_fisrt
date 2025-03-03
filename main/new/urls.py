from django.urls import path
from .views import UserRegistrationView ,UserLoginView,LogOutView,SandPasswordResetSandEmailView,SandPasswordResetView

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view()), 
    path('api/login/', UserLoginView.as_view()), 
    path('api/sand-paawordreset-email/', SandPasswordResetSandEmailView.as_view()), 
    path('reset-password/<uid>/<token>/',SandPasswordResetView.as_view()),
    path('api/logout/',LogOutView.as_view()),
]
