from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company

# Create your views here.
#
# # register applicant only
# def register_applicant(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#                 var = form.save(commit=False)
#                 var.is_applicant = True  # Custom field on the user model
#                 var.username = var.email
#                 var.save()  # Save the user instance
#                 Resume.objects.create(user=var)
#                 messages.success(request, 'Your Account has been Registered successfully! Please Login')
#                 return redirect('login')
#         else:
#             messages.warning(request, 'Something went wrong')
#             return redirect('register-applicant')
#     else:
#         form = RegisterUserForm()
#         context = {'form': form}
#         return render(request, 'users/register_applicant.html', context)

def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            try:
                # Create the user instance
                var = form.save(commit=False)
                var.is_applicant = True  # Mark as applicant
                var.username = var.email  # Use email as username
                var.save()  # Save user to the database

                # Create the associated Resume
                Resume.objects.create(user=var)

                # Success message and redirect
                messages.success(request, 'Your Account has been Registered successfully! Please Login')
                return redirect('login')
            except Exception as e:
                # Catch unexpected errors during save
                messages.error(request, f'An error occurred: {str(e)}')
                return redirect('register-applicant')
        else:
            # Display form errors in debug mode
            print(form.errors.as_json())  # Log errors in the console for debugging
            messages.error(request, 'Form validation failed. Please check your input.')
    else:
        form = RegisterUserForm()

    # Render the registration page
    context = {'form': form}
    return render(request, 'users/register_applicant.html', context)


# register recruiter only
def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True  # Custom field on the user model
            var.username = var.email
            var.save()  # Save the user instance
            Company.objects.create(user=var)
            messages.success(request, 'Your Account has been Registered successfully! Please Login')
            return redirect('login')  # Replace 'login' with the correct URL name
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('register-recruiter')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register_recruiter.html', context)

# # Login a user
# def login_user(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         user = authenticate(request, username=email, password=password)
#         if user is not None and user.is_active:
#             login(request, user)
#             return redirect('dashboard')
#             # if request.user.is_applicant:
#             #     return redirect('applicant-dashboard')
#             # elif request.user.is_recruiter:
#             #     return redirect('recruiter_dashboard')
#             # else:
#             #     return redirect('login')
#         else:
#             messages.warning(request, 'Something went wrong')
#             return redirect(request, 'users/login.html')
#     else:
#         return render(request, 'users/login.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # Redirect to dashboard after successful login
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')
    return render(request, 'users/login.html')


# Logout a user
def logout_user(request):
    logout(request)
    messages.info(request, 'Your session has ended')
    return redirect('login')


