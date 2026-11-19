from django.shortcuts import render
from .models import ImageModel
from django.db.models import Q
# Create your views here.

def main(request):
    images = ImageModel.objects.filter(is_active=True).order_by('?')[:8]
    return render(request, 'main.html', {'images': images})

def gallery(request):
    search_query = request.GET.get('q', '')
    images = ImageModel.objects.filter(is_active=True)
    if search_query:
        images = images.filter(
            Q(name__icontains=search_query.lower()) |
            Q(description__icontains=search_query.lower())
            )
    images = images.order_by('-updated_at')

    return render(request, 'gallery.html', {'images': images, 'search_query':search_query})

