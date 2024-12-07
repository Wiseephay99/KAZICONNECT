from django.shortcuts import render, redirect
from django.contrib import messages

from .form import UpdateCompanyForm
from .models import Company
from users.models import User

# Create your views here.

# update Company
def update_company(request):
    if request.user.is_recruiter:
        company =  Company.objects.get(user=request.user)
        if request.method == 'POST':
            form = UpdateCompanyForm(request.POST, instance=company)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                user.has_company = True
                var.save()
                user.save()
                messages.success(request, 'Your company info has been updated!')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went wrong')
        else:
            form = UpdateCompanyForm(instance=company)
            context = {'form': form}
            return render(request, 'company/update_company.html', context)
    else:
        messages.warning(request, 'permission denied')
        return  redirect('dashboard')

# def update_company(request):
#     # Check if the recruiter already has a company
#     try:
#         company = Company.objects.get(user=request.user)
#     except Company.DoesNotExist:
#         # Create a new company instance for the user if they don't have one
#         company = Company(user=request.user)
#
#     if request.method == 'POST':
#         form = UpdateCompanyForm(request.POST, instance=company)
#         if form.is_valid():
#             var = form.save(commit=False)
#             user = request.user  # No need to fetch the user object again
#             user.has_company = True
#             var.save()
#             user.save()
#             messages.info(request, 'Your company is now active. You can start creating job ads.')
#             return redirect('dashboard')
#         else:
#             messages.warning(request, 'Something went wrong. Please check your input.')
#     else:
#         form = UpdateCompanyForm(instance=company)
#
#     context = {'form': form}
#     return render(request, 'company/update_company.html', context)


# view company details
def company_details(request, pk):
    company = Company.objects.get(pk=pk)
    context = {'company': company}
    return render(request, 'company/company_details.html')