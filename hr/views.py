from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def hr_dashboard(request):
    return render(request, 'hr/dashboard.html')
