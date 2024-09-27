from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.shortcuts import render 



def imageshome(request):
    return render(request, "images/images.html")

def show_image(request, image_id):
    return render(request, 'images/images.html', {'image_id': image_id})