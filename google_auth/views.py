from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def homepage(request):
    name = request.user.first_name + " " + request.user.last_name
    return render(request, "home.html", {'name': name})

@login_required
def edit_details(request):
    pass
