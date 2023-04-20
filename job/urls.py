from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.jobList),
    path('<int:id>', views.jobDetails),
]
