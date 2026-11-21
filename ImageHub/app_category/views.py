from django.db.models import Q
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
    search_query = request.GET.get('q', '')
    images = ImageModel.objects.filter(category=category,is_active=True)
    if search_query:
        images = images.filter(
            Q(name__icontains=search_query.lower()) |
            Q(description__icontains=search_query.lower())
        )

    sort_by = request.GET.get('sort', 'newest')
    if sort_by == 'oldest':
        images = images.order_by('created_at')
    else:
        images = images.order_by('-created_at')

    return render(request, 'category_detail.html', {'images': images, 'search_query': search_query,
                                            'sort_by': sort_by, 'category':category})

