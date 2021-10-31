from .models import Product, ProductAttribute
from django.db.models import Max, Min


def get_filters(request):
    cats = Product.objects.distinct().values('category__title', 'category__id')
    bands = Product.objects.distinct().values('brand__title', 'brand__id')
    colors = ProductAttribute.objects.distinct().values('color__title', 'color__id', 'color__color_code')
    sizes = ProductAttribute.objects.distinct().values('size__title', 'size__id')
    minMaxPrice = ProductAttribute.objects.aggregate(Min('price'), Max('price'))
    data = {
        'cats': cats,
        'bands': bands,
        'colors': colors,
        'sizes': sizes,
        'minMaxPrice': minMaxPrice,
    }
    return data
