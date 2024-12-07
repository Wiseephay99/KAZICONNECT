from django.urls import path
from . import views
from .views import dashboard


urlpatterns = [
    # deleted initially
    # path('', views.proxy, name='proxy'),
    # path('applicant-dashboard/', views.applicant_dashboard, name='applicant-dashboard'),
    # path('recruiter-dashboard', views.recruiter_dashboard, name='recruiter-dashboard')
    path('', dashboard, name='dashboard'),  # Root path for the dashboard app
]