from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def homepage(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    return render(request, "home.html", {'profile': user_profile})

@login_required
def edit_profile(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        bio = request.POST.get("bio")
        user_profile.bio = bio
        user_profile.save()
        if request.FILES:
            print("File")
        return redirect('/')
    else:
        return render(request, 'edit_details.html', {'profile':user_profile})
