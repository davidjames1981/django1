from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.shortcuts import render 


def imageshome(request):
    return render(request, "images/images.html")