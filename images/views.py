from PIL import Image
import os
from django.conf import settings
from django.shortcuts import render, redirect

def images_home(request):
    return render(request, 'images/images.html')  # For /images/

def show_image(request, image_id):
    # Define the folder where images are stored
    image_folder = settings.MEDIA_ROOT
    image_path = os.path.join(image_folder, f'{image_id}.png')  # Now only using .png files

    if request.method == 'POST' and 'image' in request.FILES:
        uploaded_image = request.FILES['image']
        
        # Open the uploaded image using Pillow
        img = Image.open(uploaded_image)

        # Ensure the image has an alpha channel
        img = img.convert("RGBA")

        # Create a white background with the same size
        white_background = Image.new("RGBA", img.size, (255, 255, 255, 255))
        
        # Paste the original image onto the white background
        white_background.paste(img, (0, 0), mask=img)

        # Convert to RGB to remove alpha and keep white background
        final_img = white_background.convert("RGB")

        # Save the new image over the original file
        final_img.save(image_path, format='PNG')

        return redirect('show_image', image_id=image_id)

    # Check if the image exists
    if os.path.exists(image_path):
        image_url = f'{settings.MEDIA_URL}{image_id}.png'  # Serve the .png file
        return render(request, 'images/image_template.html', {'image_url': image_url, 'image_found': True, 'image_string': image_id})
    else:
        return render(request, 'images/image_template.html', {'image_found': False, 'image_string': image_id})
