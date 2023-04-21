from django.shortcuts import render
from . models import JobModel

# Create your views here.


def home(request):
    return render(request, 'pages/home.html')

def jobList(request):
    
    context= {
        'jobs': JobModel.objects.all()
    }
    return render(request, 'pages/jobList.html', context)

def jobDetails(request, id):
    context= {
        'jobs': JobModel.objects.get(id=id)
    }
    return render(request, 'pages/jobDetails.html', context)