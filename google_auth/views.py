from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def homepage(request):
    get_object_or_404(Profile, user=request.user)
    return render(request, "home.html", {'name': name})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        return redirect('/')
    else:
        return render(request, 'edit_details.html')
