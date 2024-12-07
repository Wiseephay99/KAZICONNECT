import django_filters
from job.models import Job

class Jobfilter(django_filters.FilterSet):
    # enables filter based on a single word and checks if it maches
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ['title', 'state', 'job_type', 'industry']