from django.shortcuts import render
from .models import ImageModel

# Create your views here.

def main(request):
    images = ImageModel.objects.filter(is_active=True).order_by('?')[:8]
    return render(request, 'main.html', {'images': images})

