from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from urllib3 import request

from .models import Job, ApplyJob
from .form import CreateJobForm, UpdateJobForm


# Create your views here.


# create a job
def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreateJobForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company = request.user.company
                var.save()
                messages.info(request, 'New Job has been Created!')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went wrong')
                return redirect('create-job')
        else:
            form = CreateJobForm()
            context = {'form': form}
            return render(request, 'job/create_job.html', context)
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')


# create a job
def update_job(request, pk):
    # job = Job.objects.get(pk=pk)
    job = get_object_or_404(Job, pk=pk)  # Fetch the job instance
    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job) # # Bind the job instance to the form
        if form.is_valid():
            form.save()
            messages.info(request, 'Job info has been updated!')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = UpdateJobForm(instance=job)  # Pre-fill the form with job data)
        context = {'form': form, 'job':job}
        return render(request, 'job/update_job.html', context)

def manage_jobs(request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context = {'jobs':jobs}
    return render(request, 'job/manage_jobs.html', context)

def apply_to_job(request, pk):
    if request.user.is_authenticated and request.user.is_applicant:
        # job = Job.objects.get(pk=pk)
        # Retrieve the job, ensuring it exists
        job = get_object_or_404(Job, pk=pk)

        # Check if the user has already applied for the job
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            messages.warning(request, 'Permission Denied')
            return redirect('dashboard')
        else:
            # Create the application if the user hasn't applied yet
            ApplyJob.objects.create(
                job=job,
                user= request.user,
                status = 'Pending'
            )
            messages.success(request, 'You have successfully applied! Please see your dashboard')
            return redirect('dashboard')
    else:
        # Redirect unauthenticated users to the login page
        messages.info(request, 'Please Login to Apply!')
        return redirect('login')


def all_applicants(request, pk):
    job = Job.objects.get(pk=pk)
    applicants = job.applyjob_set.all()
    context =  {'job':job, 'applicants':applicants}
    return render(request, 'job/all_applicants.html', context)
    # resume

def applied_jobs(request):
    jobs = ApplyJob.objects.filter(user=request.user)
    context = {'jobs':jobs}
    return render(request, 'job/applied_jobs.html', context)