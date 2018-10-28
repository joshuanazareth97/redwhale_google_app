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
        image_file = request.FILES.get("display")
        if image_file:
            ext = image_file.name.split(".")[-1]
            size = image_file.size/1024**2
            print(ext,size)
            if ext in ["png","jpg","bmp","gif", "jpeg"] and size < 50:
                user_profile.display_picture.save("{}.{}".format(user_profile.user,ext),image_file)
            else:
                print("Error")
                return render(request, "edit_details.html", {'profile': user_profile, 'error': "Please enter a valid image. [PNG, JPG, GIF, BMP]"})
        return redirect('/')
    else:
        return render(request, 'edit_details.html', {'profile':user_profile})
