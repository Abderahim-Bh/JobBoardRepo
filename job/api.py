from . serializers  import JobSerializer
from . models import JobModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics



@api_view(['GET'])
def jobListApi(request):
    jobs = JobModel.objects.all()
    data = JobSerializer(jobs, many= True).data
    return Response({'data':data})

@api_view(['GET'])
def jobDetailApi(request, id):
    job = JobModel.objects.get(id=id)
    data = JobSerializer(job).data
    return Response({'data':data})


class JobListApi(generics.ListAPIView):
    queryset = JobModel.objects.all()
    serializer_class = JobSerializer


class JobDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobModel.objects.all()
    serializer_class = JobSerializer
    lookup_field = "id"