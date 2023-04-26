from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signUp, name='signUpPage'),
    path('profile', views.profile, name='profilePage'),
    path('profile/editProfile', views.editProfile, name='editProfilePage'),
]