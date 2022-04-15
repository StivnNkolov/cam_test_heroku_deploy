from django.contrib.auth.views import LogoutView
from django.urls import path

from cam_0504.accounts.views import RegisterUserView, LogInView, ChangeUserPasswordView, ProfileDetailsView, \
    ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('log-in/', LogInView.as_view(), name='log in'),
    path('log-out/', LogoutView.as_view(), name='logout'),
    path('change_password/<int:pk>/', ChangeUserPasswordView.as_view(), name='change password'),

    path('profile/details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile edit'),
    path('profile/delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete'),

]
