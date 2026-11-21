from django.shortcuts import render, get_object_or_404
from app.models import ImageModel, CategoryModel

# Create your views here.

def categories(request):
    categories = CategoryModel.objects.all()
    category_data = []

    for category in categories:
        image = ImageModel.objects.filter(
            category=category,
            is_active=True
        ).first()

        category_data.append({
            'category': category,
            'image': image
        })

    return render(request, 'categories.html', {'category_data':category_data })

def category_detail(request, category):
    category = get_object_or_404(CategoryModel, name=category)
    images = ImageModel.objects.filter(category=category,is_active=True)

    return render(request, 'categories.html', {'images': images})

