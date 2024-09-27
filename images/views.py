from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.shortcuts import render 



def images_home(request):
    return render(request, 'images/images.html')  # For /images/

def show_image(request, image_id):
    return render(request, 'images/image_template.html', {'image_id': image_id})  # For /images/123
