from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, VerificationCode

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('confirm_email/', VerificationCode.as_view(), name='confirm_email')
]