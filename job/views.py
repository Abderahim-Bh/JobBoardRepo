from django.shortcuts import render

# Create your views here.


def jobList(request):
    return render(request, 'jobList.html')

def jobDetails(request, id):
    pass