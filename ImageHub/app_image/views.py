from django.shortcuts import render, get_object_or_404
from app.models import ImageModel

# Create your views here.

def image_detail(request, image_id):
    image = get_object_or_404(ImageModel, pk=image_id, is_active=True)
    return render(request, 'image_detail.html', {'image': image})
