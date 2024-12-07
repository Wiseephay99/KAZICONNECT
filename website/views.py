from django.shortcuts import render, get_object_or_404
from job.models import Job, ApplyJob
from .filter import Jobfilter

# Create your views here.

def home(request):
    # Fetch available jobs and apply the filter (if needed)
    filter = Jobfilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))
    context = {'filter': filter}
    return render(request, 'website/home.html', context)


def job_listing(request):
    jobs =  Job.objects.filter(is_available=True).order_by('-timestamp')
    context = {'jobs': jobs}
    return render(request, 'website/job_listing.html', context)

# def job_details(request, pk):
#     # Make an applicant only apply once per job
#     if ApplyJob.objects.filter(user=request.user, job=pk).exists():
#         has_applied = True
#     else:
#         has_applied = False
#     job =  Job.objects.get(pk=pk)
#     context = {'job': job}
#     return render(request, 'website/job_details.html', context)

def job_details(request, pk):
    # Retrieve the job details
    job = get_object_or_404(Job, pk=pk)
    # Check if the user is authenticated
    has_applied = False
    if request.user.is_authenticated:
        # Check if the user has already applied for this job
        has_applied = ApplyJob.objects.filter(user=request.user, job=job).exists()
    context = {
        'job': job,
        'has_applied': has_applied,
    }
    return render(request, 'website/job_details.html', context)
