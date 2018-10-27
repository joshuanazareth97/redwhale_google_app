from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def homepage(request):
    return render(request, "home.html")
