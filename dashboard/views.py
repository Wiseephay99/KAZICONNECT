from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

# def proxy(request):
#     if request.user.is_applicant:
#         return redirect('applicant-dashboard')
#     elif request.user.is_recruiter:
#         return redirect('recruiter-dashboard')
#     else:
#         return redirect('login')
#
# def applicant_dashboard(request):
#     return render(request, 'dashboard/applicant_dashboard.html')
#
# def recruiter_dashboard(request):
#     return render(request, 'dashboard/recruiter_dashboard.html')

@login_required(login_url='login')  # Redirect unauthenticated users to the login page
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


# @login_required
# def dashboard(request):
#     if request.user.is_applicant:
#         return render(request, 'dashboard/applicant_dashboard.html')
#     elif request.user.is_recruiter:
#         return render(request, 'dashboard/recruiter_dashboard.html')
#     else:
#         return redirect('some-default-page')  # Redirect to a default page if the role is not defined