import django_filters
from . models import JobModel

class jobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = JobModel
        fields = ['title', 'jobType', 'description', 'experience', 'category']