from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('jobs', views.jobList),
    path('jobs/<int:id>', views.jobDetails),
]

