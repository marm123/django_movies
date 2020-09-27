from django.urls import path

from accounts.views import SubmittableLoginView, SubmittablePasswordChangeView, SuccessMessagedLogoutView, SignUpView

app_name = 'accounts'

urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', SuccessMessagedLogoutView.as_view(), name='logout'),
    path('passwordchange/', SubmittablePasswordChangeView.as_view(), name='passchange'),
    path('register/', SignUpView.as_view(), name='register')
]
