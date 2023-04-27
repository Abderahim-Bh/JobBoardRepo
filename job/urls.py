from django.urls import path, include
from . import views
from . import api 

urlpatterns = [
    path('', views.home, name='homePage'),
    path('jobs', views.jobList,name='jobListPage'),
    path('jobs/<str:slug>', views.jobDetails,name='jobDetailsPage'),
    path('postJob', views.postJob, name='postJobPage'),
    
    #api
    path('api/list', api.jobListApi , name='jobListApi'),
    path('api/list/<int:id>', api.jobDetailApi , name='jobDetailApi'),

    #class based views
    path('api/v2/list', api.JobListApi.as_view() , name='JobListApiV2'),
    path('api/v2/list/<int:id>', api.JobDetailApi.as_view() , name='JobDetailApiV2'),

]

