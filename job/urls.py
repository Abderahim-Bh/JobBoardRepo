from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
    path('jobs', views.jobList,name='jobListPage'),
    path('jobs/<str:slug>', views.jobDetails,name='jobDetailsPage'),
]

