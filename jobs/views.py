from django.shortcuts import render
from .models import jobs

def home(request):
    job = jobs.objects
    return render(request, 'jobs/templates/jobs/home.html',{ 'job':job } )
