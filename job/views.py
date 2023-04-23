from django.shortcuts import render
from . models import JobModel
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    context= {
        'jobs': JobModel.objects.all(),
        'jobsCount': JobModel.objects.count(),
    }
    return render(request, 'pages/home.html', context)

def jobList(request):
    
    jobsObject = JobModel.objects.all()
    paginator = Paginator(jobsObject,1)
    pageNumber = request.GET.get('page')
    pageObject = paginator.get_page(pageNumber)

    context= {
        'jobs': pageObject,
        'jobsCount': JobModel.objects.count(), 
    }
    return render(request, 'pages/jobList.html', context)

def jobDetails(request, slug):
    context= {
        'job': JobModel.objects.get(slug=slug)
    }
    return render(request, 'pages/jobDetails.html', context)