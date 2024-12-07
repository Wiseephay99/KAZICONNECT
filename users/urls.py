from django.urls import path
from . import views

urlpatterns = [
    path('register-applicant/', views.register_applicant, name='register-applicant'),
    path('register-recruiter/', views.register_recruiter, name='register-recruiter'),
    path('login/', views.login_user, name='login'),  # Fix: use the login view instead of logout_user
    path('logout/', views.logout_user, name='logout'),
]
