from django.shortcuts import redirect, render
from . models import JobModel
from django.core.paginator import Paginator
from . forms import ApplyForm, JobModelForm
from django.contrib.auth.decorators import login_required
from . filters import jobFilter

# Create your views here.


def home(request):
    context= {
        'jobs': JobModel.objects.all(),
        'jobsCount': JobModel.objects.count(),
    }
    return render(request, 'pages/home.html', context)

def jobList(request):
    
    jobsObject = JobModel.objects.all()
    myFilter = jobFilter(request.GET, queryset=jobsObject)
    jobsObject = myFilter.qs

    paginator = Paginator(jobsObject,5)
    pageNumber = request.GET.get('page')
    pageObject = paginator.get_page(pageNumber)

    context= {
        'jobs': pageObject,
        'jobsCount': JobModel.objects.count(),
        'myFilter' : myFilter 
    }
    return render(request, 'pages/jobList.html', context)




def jobDetails(request, slug):
    jobObject = JobModel.objects.get(slug=slug)
    if request.method=="POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = jobObject
            myform.save()
            
    else:
        form = ApplyForm

    context= {
        'job': jobObject,
        'form': form,
    }
    return render(request, 'pages/jobDetails.html', context)


@login_required
def postJob(request):

    if request.method == "POST":
        form = JobModelForm(request.POST, request.FILES )
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect("/")
    else:
        form = JobModelForm


    contex = {
        'form' : form
    }
    return render(request, 'pages/postJob.html', contex)